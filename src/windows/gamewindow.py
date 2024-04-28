from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton
from widgets.game import GameField


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def init_start_button(self):
        self.start_button = QPushButton("Начать игру", self)
        self.start_button.setGeometry(50, 50, 150, 30)
        self.start_button.clicked.connect(self.start_game)

    def init_name_input(self):
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(450, 50, 150, 30)
        self.name_input.setPlaceholderText("Введите свое имя")

    def init_score_label(self):
        self.score_text = "Счёт: %d"
        self.score_label = QLabel(self)
        self.score_label.setGeometry(300, 50, 60, 30)

    def start_game(self):
        self.game_field.setFocus()
        self.game_field.start_game()

    def initUI(self):
        self.setWindowTitle('Игра')
        self.setGeometry(300, 300, 650, 650)
        self.init_start_button()
        self.init_name_input()
        self.init_score_label()
        self.game_field = GameField(self)

