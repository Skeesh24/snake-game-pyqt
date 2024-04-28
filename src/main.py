from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from database import get_leaderboard_data
from windows.gamewindow import GameWindow
from windows.infowindow import InfoWindow
from windows.leaderboard import LeaderboardWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Главное меню")
        self.setGeometry(300, 300, 300, 300)
        self.init_leaderboard_button()
        self.init_game_button()
        self.init_info_button()

    def init_leaderboard_button(self):
        self.open_rating_button = QPushButton("Рейтинг", self)
        self.open_rating_button.move(100, 100)
        self.open_rating_button.clicked.connect(self.open_leaderboard)

    def init_game_button(self):
        self.open_rating_button = QPushButton("Игра", self)
        self.open_rating_button.move(100, 50)
        self.open_rating_button.clicked.connect(self.open_game)

    def init_info_button(self):
        self.open_rating_button = QPushButton("Правила игры", self)
        self.open_rating_button.move(100, 150)
        self.open_rating_button.clicked.connect(self.open_info)

    def open_leaderboard(self):
        self.leaderboard_window = LeaderboardWindow()
        self.leaderboard_window.show()
        leaderboard_data = get_leaderboard_data()
        self.leaderboard_window.update_leaderboard(leaderboard_data)

    def open_game(self):
        self.game_window = GameWindow()
        self.game_window.show()

    def open_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()


def main():
    app = QApplication([])
    mainform = Main()
    mainform.show()
    app.exec_()


if __name__ == "__main__":
    main()
