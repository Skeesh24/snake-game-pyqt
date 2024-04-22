import random

from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget

from database import add_to_leaderboard
from resources import RES_BACKGROUND


class GameField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.form = parent
        self.initGameField()

    def initGameField(self):
        self.background = QPixmap(RES_BACKGROUND)
        self.setGeometry(50, 100, 550, 500)
        self.reset_game_parameters()
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_snake)
        self.spawn_fruit()

    def start_game(self):
        self.timer.start(100)

    def spawn_fruit(self):
        max_x = self.width() // 10
        max_y = self.height() // 10
        self.fruit = QPoint(random.randint(0, max_x), random.randint(0, max_y))
        if self.fruit.x() not in range(51) or self.fruit.y() not in range(51):
            self.spawn_fruit()

    def move_snake(self):
        head = self.snake[0] + self.direction
        if head == self.fruit:
            self.spawn_fruit()
            self.score += 10
            self.form.score_label.setText(self.form.score_text % self.score)
        else:
            self.snake.pop()

        if head in self.snake or not self.valid_position(head):
            self.timer.stop()
            self.end_game()
            return

        self.snake.insert(0, head)
        self.update()

    def valid_position(self, point):
        return (0 <= point.x() < self.width() // 10) and (
            0 <= point.y() < self.height() // 10
        )

    def end_game(self):
        current_name = self.form.name_input.text()
        add_to_leaderboard(current_name or "Аноним", self.score)
        self._end_messagebox()

    def _end_messagebox(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText("You lost! Play again?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.buttonClicked.connect(self._handle_game_over_button)
        msg_box.exec_()

    def _handle_game_over_button(self, button):
        self.reset_game_parameters()
        if button.text() == "&No":
            self.timer.stop()
        if button.text() == "&Yes":
            self.spawn_fruit()
            self.timer.start(100)
            self.update()

    def reset_game_parameters(self):
        self.snake = [QPoint(5, 5)]
        self.fruit = QPoint(0, 0)
        self.direction = QPoint(1, 0)
        self.score = 0
        self.form.score_label.setText(self.form.score_text % 0)

    def paintEvent(self, _):
        qp = QPainter(self)
        qp.drawPixmap(self.rect(), self.background)

        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(self.fruit.x() * 10, self.fruit.y() * 10, 10, 10)

        qp.setBrush(QColor(0, 255, 0))
        for p in self.snake:
            qp.drawRect(p.x() * 10, p.y() * 10, 10, 10)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_W and self.direction != QPoint(0, 1):
            self.direction = QPoint(0, -1)
        elif key == Qt.Key_S and self.direction != QPoint(0, -1):
            self.direction = QPoint(0, 1)
        elif key == Qt.Key_A and self.direction != QPoint(1, 0):
            self.direction = QPoint(-1, 0)
        elif key == Qt.Key_D and self.direction != QPoint(-1, 0):
            self.direction = QPoint(1, 0)
