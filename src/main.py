from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton

from database import get_leaderboard_data, init_database
from src.widgets.game import GameField
from src.windows.leaderboard import LeaderboardWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        init_database()
        self.initUI()

    def init_start_button(self):
        self.start_button = QPushButton("Start Game", self)
        self.start_button.move(50, 50)
        self.start_button.clicked.connect(self.start_game)

    def init_leaderboard_button(self):
        self.open_rating_button = QPushButton("Leaderboard", self)
        self.open_rating_button.move(500, 50)
        self.open_rating_button.clicked.connect(self.open_leaderboard)

    def init_name_input(self):
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(250, 50, 150, 30)
        self.name_input.setPlaceholderText("Enter your name")
    
    def get_name(self):
        return self.name_input.text()

    def initUI(self):
        self.setWindowTitle("Snake Game")
        self.setGeometry(300, 300, 650, 650)
        self.init_start_button()
        self.init_leaderboard_button()
        self.init_name_input()
        self.game_field = GameField(self)

    def start_game(self):
        self.game_field.setFocus()
        self.game_field.start_game()

    def open_leaderboard(self):
        self.leaderboard_window = LeaderboardWindow()
        self.leaderboard_window.show()
        leaderboard_data = get_leaderboard_data()
        self.leaderboard_window.update_leaderboard(leaderboard_data)


def main():
    app = QApplication([])
    mainform = Main()
    mainform.show()
    app.exec_()


if __name__ == "__main__":
    main()
