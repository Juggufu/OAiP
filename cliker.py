from PyQt5.QtWidgets import *


class ClicedApp(QWidget):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.unitUI()


    def unitUI(self):
        self.resize(400, 50)
        self.setWindowTitle('Clicer')

        button = QPushButton('Кликер')
        self.label = QLabel('количество кликов: 0')

        main_l = QVBoxLayout()
        h_l = QHBoxLayout()

        main_l.addStretch()
        main_l.addWidget(button)
        main_l.addWidget(self.label)
        h_l.stretch(2)
        main_l.addLayout(h_l)

        self.setLayout(main_l)
        button.clicked.connect(self.click)

    def click(self):
        self.clicks += 1
        self.label.setText(f'количество кликов:{self.clicks}')


def main():
    app = QApplication([])
    win = ClicedApp()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()