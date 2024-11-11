from PyQt6.QtWidgets import *
from collections import Counter

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(700, 500)
        self.setWindowTitle('Текстовый редактор')

        self.name_file = QLineEdit()
        button = QPushButton('Создать файл')
        button2 = QPushButton('Сохранить файл')
        button3 = QPushButton('Открыть файл')
        self.text = QTextEdit()
        self.text.textChanged.connect(self.analyze_text)

        self.num_letters = QLabel('Количество символов: ')
        self.num_word = QLabel('Количество слов: ')
        self.long_word = QLabel('Самое длинное слово: ')
        self.short_word = QLabel('Самое короткое слово: ')
        self.often_word = QLabel('Слово, которое чаще всего встречалось: ')

        main_l = QHBoxLayout()
        main_ll = QVBoxLayout()
        main_lll = QVBoxLayout()

        main_ll.addWidget(self.name_file)
        main_ll.addWidget(button)
        main_ll.addWidget(button2)
        main_ll.addWidget(button3)
        main_ll.addWidget(self.num_letters)
        main_ll.addWidget(self.num_word)
        main_ll.addWidget(self.long_word)
        main_ll.addWidget(self.short_word)
        main_ll.addWidget(self.often_word)
        main_lll.addWidget(self.text)
        main_ll.addStretch()

        main_l.addStretch()
        main_l.addLayout(main_ll, 2)
        main_l.addLayout(main_lll, 3)
        main_l.addStretch()

        self.setLayout(main_l)
        button.clicked.connect(self.create_file)
        button2.clicked.connect(self.save_file)
        button3.clicked.connect(self.open_file)

    def create_file(self):
        with open(self.name_file.text(), 'w', encoding='utf-8') as file:
            file.write(self.text.toPlainText())

    def save_file(self):
        with open(self.name_file.text(), 'w', encoding='utf-8') as file:
            file.write(self.text.toPlainText())

    def open_file(self):
        with open(self.name_file.text(), 'r', encoding='utf-8') as file:
            text = file.read()
            self.text.setPlainText(text)
        self.analyze_text()

    def analyze_text(self):
        text_content = self.text.toPlainText()

        num_letters = len(text_content)
        words = text_content.split()
        num_words = len(words)

        if words:
            longest_word = max(words, key=len)
            shortest_word = min(words, key=len)
            most_common_word = Counter(words).most_common(1)[0][0]
        else:
            longest_word = ""
            shortest_word = ""
            most_common_word = ""

        self.num_letters.setText(f'Количество символов: {num_letters}')
        self.num_word.setText(f'Количество слов: {num_words}')
        self.long_word.setText(f'Самое длинное слово: {longest_word}')
        self.short_word.setText(f'Самое короткое слово: {shortest_word}')
        self.often_word.setText(f'Слово, которое чаще всего встречалось: {most_common_word}')


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
