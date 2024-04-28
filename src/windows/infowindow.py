from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton
from widgets.game import GameField


class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сведения')
        self.setGeometry(300, 300, 650, 650)
        self.label = QLabel(self)
        self.label.setText("Правила игры: \n Собирать фрукты, не врезаться в стены или собственный хвост.") 

