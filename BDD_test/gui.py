from PyQt6.QtWidgets import *


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Нажмите кнопку для открытия окна")
        layout.addWidget(self.label)

        self.button = QPushButton("Открыть окно")
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec()
