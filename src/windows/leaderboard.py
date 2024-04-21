from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class LeaderboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Leaderboard')
        self.setGeometry(400, 400, 300, 200)
        layout = QVBoxLayout(self)
        
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Player', 'Score'])
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)        
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def update_leaderboard(self, data):
        self.table_widget.setRowCount(len(data))
        for i, (player, score) in enumerate(data):
            self.table_widget.setItem(i, 0, QTableWidgetItem(player))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(score)))   
