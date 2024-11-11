from PyQt6.QtWidgets import *
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform
from PyQt6.QtCore import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.original_image = None

    def initUI(self):
        self.resize(400, 600)
        self.setWindowTitle('редактор изображений')

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_dowland = QPushButton('загруить изображение', self)
        self.button_dowland.clicked.connect(self.dowland_image)

        self.button_turn_left = QPushButton('повернуть фото на 90 градусов в лево', self)
        self.button_turn_left.clicked.connect(self.turn_left)

        self.button_turn_right = QPushButton('повернуть фото на 90 градусов в вправо', self)
        self.button_turn_right.clicked.connect(self.turn_right)

        self.button_r = QPushButton('отобразить цветовой канал R', self)
        self.button_r.clicked.connect(self.colorR)

        self.button_g = QPushButton('отобразить цветовой канал G', self)
        self.button_g.clicked.connect(self.colorG)

        self.button_b = QPushButton('отобразить цветовой канал B', self)
        self.button_b.clicked.connect(self.corolB)

        self.button_all_rgb = QPushButton('отобразить все цветовые каналы', self)
        self.button_all_rgb.clicked.connect(self.corolall)

        self.slide = QSlider(self)
        self.slide.setRange(0, 500)
        self.slide.setValue(500)
        self.slide.valueChanged.connect(self.transparency)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addStretch()
        layout2.addWidget(self.button_dowland)
        layout2.addWidget(self.button_turn_left)
        layout2.addWidget(self.button_turn_right)
        layout2.addWidget(self.button_r)
        layout2.addWidget(self.button_g)
        layout2.addWidget(self.button_b)
        layout2.addWidget(self.button_all_rgb)
        layout3.addWidget(self.slide)
        layout2.addWidget(self.image_label)

        layout1.addStretch()
        layout1.addLayout(layout2, 2)
        layout1.addLayout(layout3, 3)
        layout1.addStretch()
        self.setLayout(layout1)

        self.image = None

    def dowland_image(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'Открыть изображение', '',
                                                  'Images (*.png *.jpg *.bmp)')
        if filepath:
            self.image = QImage(filepath)
            self.original_image = self.image.copy()
            self.update()

    def turn_left(self):
        if self.image:
            turn_l = QTransform().rotate(-90)
            self.image = self.image.transformed(turn_l)
            self.update()

    def turn_right(self):
        if self.image:
            turn_l = QTransform().rotate(90)
            self.image = self.image.transformed(turn_l)
            self.update()

    def colorR(self):
        if self.original_image:
            temp_image = QImage(self.original_image.size(), QImage.Format.Format_ARGB32)
            for y in range(self.original_image.height()):
                for x in range(self.original_image.width()):
                    pixel = self.original_image.pixel(x, y)
                    r = QColor(pixel).red()
                    new_pixel = QColor(r, 0, 0)
                    temp_image.setPixel(x, y, new_pixel.rgb())
            self.image = temp_image
            self.update()


    def colorG(self):
        if self.original_image:
            temp_image = QImage(self.original_image.size(), QImage.Format.Format_ARGB32)
            for y in range(self.original_image.height()):
                for x in range(self.original_image.width()):
                    pixel = self.original_image.pixel(x, y)
                    g = QColor(pixel).green()
                    new_pixel = QColor(0, g, 0)
                    temp_image.setPixel(x, y, new_pixel.rgb())
            self.image = temp_image
            self.update()


    def corolB(self):
        if self.original_image:
            temp_image = QImage(self.original_image.size(), QImage.Format.Format_ARGB32)
            for y in range(self.original_image.height()):
                for x in range(self.original_image.width()):
                    pixel = self.original_image.pixel(x, y)
                    b = QColor(pixel).blue()
                    new_pixel = QColor(0, 0, b)
                    temp_image.setPixel(x, y, new_pixel.rgb())
            self.image = temp_image
            self.update()


    def corolall(self):
        if self.original_image:
            self.image = self.original_image.copy()
            self.update()

    def transparency(self):
        if self.image:
            transparen = self.slide.value() / 500.0
            temp_pixmap = QImage(self.image.size(), QImage.Format.Format_ARGB32)
            for y in range(self.image.height()):
                for x in range(self.image.width()):
                    pixel = self.image.pixel(x, y)
                    a = QColor(pixel).alpha() * transparen
                    new_pixel = QColor(QColor(pixel).red(), QColor(pixel).green(), QColor(pixel).blue(), int(a))
                    temp_pixmap.setPixel(x, y, new_pixel.rgba())
            self.image = temp_pixmap
            self.update()

    def update(self):
        if self.image:
            pixmap = QPixmap.fromImage(self.image)
            self.image_label.setPixmap(pixmap)



def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()