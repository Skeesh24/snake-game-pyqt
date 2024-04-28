from PyQt5.QtWidgets import QLabel, QWidget

GAME_RULE_TEXT = """Инструкция пользователя: \n\n
    1. Для перехода к игре нажмите кнопку "Играть".\n
    2. Введите свое имя или псевдоним в поле ввода в правой верхной части окна.\n
    3. Нажмите кнопку "Играть" для начала выполнения кода.\n
        3.1. Вы играете за зеленую змейку.\n
        3.2. Управление очуществляется по клавишам WASD и "стрелочкам".\n
        3.3. Вам необходимо съесть как можно больше красных фруктов.\n
        3.4. Когда вы съедаете красный фрукт, ваш счет увеличивается на 10 очков.\n
        3.5 Остерегайтесь стен! При встрече с ними игра закончится.\n
    4. После окончания игры вам будет предложено сыграть еще раз.\n
    5. Для выхода из режима игры закройте окно.\n
    6. Для просмотра таблицы результатов нажмите кнопку "Рейтинг".\n
    7. Приятной игры!
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
                padding: 20px; /* Add padding around the widget */
            }
            QLabel {
                font: 14px;
                color: #fff;
                margin: 10px; /* Add margin to the label */
            }
           
        """
        )
        self.label = QLabel(self)
        self.label.setText(GAME_RULE_TEXT)
