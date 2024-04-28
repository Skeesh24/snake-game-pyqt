from PyQt5.QtWidgets import QLabel, QWidget

GAME_RULE_TEXT = """
Правила игры: 
    1. Собирать фрукты, не врезаться в стены или собственный хвост.
"""


class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Сведения")
        self.setGeometry(300, 300, 650, 650)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #333;
                color: #eee;
            }
            QLabel {
                font: 16px;
                color: #fff;
            }
        """
        )
        self.label = QLabel(self)
        self.label.setText(GAME_RULE_TEXT)
