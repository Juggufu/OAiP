from PyQt6.QtWidgets import *
import random


class Random(QWidget):
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):
        self.resize(400, 50)
        self.setWindowTitle('Random number')
        self.first = QLineEdit()
        self.first.setPlaceholderText('введите первое число')
        self.last = QLineEdit()
        self.last.setPlaceholderText('введите последнее число')
        button = QPushButton('Сгенерировать число')
        self.label = QLabel('Случайное число:')

        main_l = QVBoxLayout()
        hl = QHBoxLayout()

        main_l.addStretch()
        main_l.addWidget(button)
        main_l.addWidget(self.label)
        main_l.addWidget(self.first)
        main_l.addWidget(self.last)
        hl.addWidget(self.first, 3)
        hl.addStretch(2)
        hl.addWidget(self.last, 3)
        main_l.addLayout(hl)
        main_l.addStretch()

        self.setLayout(main_l)
        button.clicked.connect(self.random)

    def random(self):
        num1 = int(self.first.text())
        num2 = int(self.last.text())
        message_b = QMessageBox()
        message_b.setWindowTitle('рандомное число')
        self.random_number = random.randint(num1, num2)
        self.label.setText(f'Случайное число: {self.random_number}')
        message_b.exec_()


def main():
    app = QApplication([])
    win = Random()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
