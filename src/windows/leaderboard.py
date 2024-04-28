from PyQt5.QtWidgets import (
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class LeaderboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Таблица лидеров")
        self.setGeometry(300, 300, 650, 650)
        self.setStyleSheet("background-color: #333; color: #eee;")
        self.layout = QVBoxLayout(self)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Игрок", "Счет"])
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

    def update_leaderboard(self, data):
        self.table_widget.setRowCount(len(data))
        for i, (player, score) in enumerate(data):
            self.table_widget.setItem(i, 0, QTableWidgetItem(player))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(score)))
