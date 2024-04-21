from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QLabel

from database import get_leaderboard_data, init_database
from resources import init_resources
from widgets.game import GameField
from windows.leaderboard import LeaderboardWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        init_database()
        init_resources()
        self.init_UI()

    def init_start_button(self):
        self.start_button = QPushButton("Начать игру", self)
        self.start_button.move(50, 50)
        self.start_button.clicked.connect(self.start_game)

    def init_leaderboard_button(self):
        self.open_rating_button = QPushButton("Рейтинг", self)
        self.open_rating_button.move(500, 50)
        self.open_rating_button.clicked.connect(self.open_leaderboard)

    def init_name_input(self):
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(250, 50, 150, 30)
        self.name_input.setPlaceholderText("Введите свое имя")

    def init_score_label(self):
        self.score_text = "Счёт: %d"
        self.score_label = QLabel(self)
        self.score_label.setGeometry(280, 610, 60, 30)
    
    def get_name(self):
        return self.name_input.text()

    def init_UI(self):
        self.setWindowTitle("Snake Game")
        self.setGeometry(300, 300, 650, 650)
        self.init_start_button()
        self.init_leaderboard_button()
        self.init_name_input()
        self.init_score_label()
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
