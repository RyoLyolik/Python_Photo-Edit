from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
from PIL import Image
from math import pi, sqrt
from PyQt5.QtCore import *
import random

radius = 0


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_list = []
        self.index = 0
        self.open_win()

    def open_win(self):
        self.setGeometry(400, 100, 720, 480)
        self.setWindowTitle('Title')
        control = self.contr()
        main_widg = QWidget()
        main_widg.setLayout(control)
        self.setCentralWidget(main_widg)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        filemenu.addAction(self.new_file())
        self.rect = False
        self.ellipse = False
        # self.test()
        self.show()

    def contr(self):
        self.main_layout = QVBoxLayout()
        self.bottom_control = QHBoxLayout()
        self.photo_area = QHBoxLayout()
        self.top_control = QVBoxLayout()
        self.edit_photo_control = QHBoxLayout()

        self.input = QLineEdit()

        self.show_photo = QPushButton('Show')
        self.show_photo.clicked.connect(self.show_ph)

        self.top_control.addWidget(self.input)
        self.top_control.addWidget(self.show_photo)

        self.next_photo = QPushButton('Next', self)
        self.previous_photo = QPushButton('Previous', self)
        self.next_photo.clicked.connect(self.next)
        self.previous_photo.clicked.connect(self.previous)

        self.buaty_label = QLabel('', self)
        self.buaty_label2 = QLabel('', self)
        self.buaty_label.setFixedSize(200, 1)
        self.buaty_label2.setFixedSize(100, 1)

        self.info_label = QLabel('info', self)

        self.bottom_control.addWidget(self.buaty_label)
        self.bottom_control.addWidget(self.previous_photo)
        self.bottom_control.addWidget(self.next_photo)
        self.bottom_control.addWidget(self.buaty_label2)
        self.bottom_control.addWidget(self.info_label)

        self.area = QLineEdit()
        self.area.move(100, 100)
        self.opacity = QLineEdit()
        self.color = QLineEdit()
        self.area.hide()
        self.ok = QPushButton('Ok', self)
        self.ok.hide()
        self.ok.clicked.connect(self.get_vignet_area)
        self.opacity.hide()
        self.color.hide()

        self.area_label = QLabel('area, %', self)
        self.opacity_label = QLabel('opacity, [0;1]', self)
        self.color_label = QLabel('color, RGB', self)

        self.area_label.hide()
        self.opacity_label.hide()
        self.color_label.hide()

        self.make_vignet = QPushButton('Виньетка', self)
        self.make_vignet.setFixedSize(60, 20)
        self.make_vignet.clicked.connect(self.vignet)
        self.fu_go_back = QPushButton('Cancel', self)
        self.fu_go_back.setFixedSize(60, 20)
        self.fu_go_back.clicked.connect(self.go_back)

        self.radio_button_1 = QRadioButton('modern art')
        self.radio_button_1.setFixedSize(100, 15)
        self.radio_button_2 = QRadioButton('Usually drawing')
        self.radio_button_2.setFixedSize(100, 15)

        self.ch_color = QPushButton(self)
        self.ch_color.move(20, 40)
        self.ch_color.setText("Choice color")
        self.ch_color.clicked.connect(self.choose_color)
        self.color_chose = "black"

        self.button_ellipse = QPushButton('ellipse')
        self.button_ellipse.setFixedSize(100, 25)
        self.button_rect = QPushButton('rect')
        self.button_rect.setFixedSize(100, 25)

        self.check_random = QCheckBox('Random')

        self.button_ellipse.clicked.connect(self.change)
        self.button_rect.clicked.connect(self.change_2)

        self.edit_photo_control.addWidget(self.check_random)
        self.edit_photo_control.addWidget(self.ch_color)
        self.edit_photo_control.addWidget(self.button_ellipse)
        self.edit_photo_control.addWidget(self.button_rect)
        self.edit_photo_control.addWidget(self.radio_button_1)
        self.edit_photo_control.addWidget(self.radio_button_2)
        self.edit_photo_control.addWidget(self.area)
        self.edit_photo_control.addWidget(self.area_label)
        self.edit_photo_control.addWidget(self.opacity)
        self.edit_photo_control.addWidget(self.opacity_label)
        self.edit_photo_control.addWidget(self.color)
        self.edit_photo_control.addWidget(self.color_label)
        self.edit_photo_control.addWidget(self.fu_go_back)
        self.edit_photo_control.addWidget(self.make_vignet)
        self.edit_photo_control.addWidget(self.ok)

        self.file = QPixmap('')
        self.label_photo = QLabel(self)
        self.label_photo.setPixmap(self.file)

        self.photo_area.addWidget(self.label_photo)

        self.main_layout.addLayout(self.top_control)
        self.main_layout.addLayout(self.edit_photo_control)
        self.main_layout.addLayout(self.photo_area)
        self.main_layout.addLayout(self.bottom_control)

        return self.main_layout

    def change(self):
        self.ellipse = True
        self.rect = False

    def change_2(self):
        self.rect = True
        self.ellipse = False

    def new_file(self):
        new_file = QAction('New file', self)
        new_file.setStatusTip('new_file')
        new_file.triggered.connect(self.make_file)
        return new_file

    def make_file(self):
        try:
            self.slider.hide()
        except:
            pass
        self.buaty_label.hide()
        self.buaty_label2.hide()
        self.ok.hide()
        self.make_vignet.hide()
        self.fu_go_back.hide()
        self.area.hide()
        self.area_label.hide()
        self.opacity.hide()
        self.show_photo.hide()
        self.next_photo.hide()
        self.previous_photo.hide()
        self.input.hide()
        self.opacity_label.hide()
        self.color.hide()
        self.opacity_label.hide()
        self.info_label.hide()
        self.color_label.hide()
        self.make_field()
        self.done_button = QPushButton('Done')
        self.done_button.clicked.connect(self.done)
        self.edit_photo_control.addWidget(self.done_button)
        self.slider = QSlider()
        self.slider.setMaximum(100)
        self.slider.setMinimum(1)
        self.slider.setValue(5)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setFixedSize(100, 10)
        self.slider.move(self.height(), self.width() / 2)
        self.main_layout.addWidget(self.slider)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_chose = color

    def make_field(self):
        #     pass
        self.file = QPixmap('')
        self.label_photo.setPixmap(self.file)
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)

    def mousePressEvent(self, Event):
        try:
            if self.radio_button_1.isChecked():
                self.modern_art(Event)
            elif self.radio_button_2.isChecked():
                self.draw_usually(Event)
        except:
            pass

    def paintEvent(self, Event):
        paint = QPainter(self)
        try:
            paint.drawImage(0, 0, self.image)
        except:
            pass

    def done(self):
        self.done_button.hide()
        self.buaty_label.show()
        self.buaty_label2.show()
        self.make_vignet.show()
        self.fu_go_back.show()
        self.show_photo.show()
        self.next_photo.show()
        self.info_label.show()
        self.previous_photo.show()
        self.input.show()
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.rect = False
        self.ellipse = False

    def mouseMoveEvent(self, Event):
        # print(Event.pos())
        if self.radio_button_1.isChecked():
            self.modern_art(Event)
        elif self.radio_button_2.isChecked():
            self.draw_usually(Event)

    def modern_art(self, Event):
        try:
            self.paint = QPainter(self.image)
            self.paint.setBrush(
                QColor(random.choice(range(0, 256)), random.choice(range(0, 256)), random.choice(range(0, 256))))
            print(self.rect)
            if self.ellipse:
                if self.check_random.isChecked():
                    self.paint.drawEllipse(random.choice(range(0, self.width())),
                                           random.choice(range(0, self.height())),
                                           random.choice(range(0, self.width())),
                                           random.choice(range(0, self.height())))
                else:
                    self.paint.drawEllipse(int(str(Event.pos())[20:-1].split(', ')[0]),
                                           int(str(Event.pos())[20:-1].split(', ')[1]),
                                           int(str(Event.pos())[20:-1].split(', ')[0]) * self.slider.value() / 10,
                                           int(str(Event.pos())[20:-1].split(', ')[1]) * self.slider.value() / 10)
            elif self.rect:
                if self.check_random.isChecked():
                    points = QPolygon(
                        [QPoint(random.choice(range(0, self.width())), random.choice(range(0, self.height()))),
                         QPoint(random.choice(range(0, self.width())), random.choice(range(0, self.height()))),
                         QPoint(random.choice(range(0, self.width())), random.choice(range(0, self.height()))),
                         QPoint(random.choice(range(0, self.width())), random.choice(range(0, self.height())))])
                    self.paint.drawPolygon(points)
                else:
                    self.paint.drawRect(int(str(Event.pos())[20:-1].split(', ')[0]),
                                        int(str(Event.pos())[20:-1].split(', ')[1]),
                                        int(str(Event.pos())[20:-1].split(', ')[0]) * self.slider.value() / 10,
                                        int(str(Event.pos())[20:-1].split(', ')[1]) * self.slider.value() / 10)
                    print(random.choice(range(0, self.width())), random.choice(range(0, self.height())), 1, 1, 1, 1, 1)

            self.update()
        except:
            pass

    def draw_usually(self, Event):
        try:
            self.paint = QPainter(self.image)
            self.paint.setBrush(QColor(self.color_chose))
            if self.ellipse:
                self.paint.drawEllipse(int(str(Event.pos())[20:-1].split(', ')[0]),
                                       int(str(Event.pos())[20:-1].split(', ')[1]), self.slider.value(),
                                       self.slider.value())
            elif self.rect:
                self.paint.drawRect(int(str(Event.pos())[20:-1].split(', ')[0]),
                                    int(str(Event.pos())[20:-1].split(', ')[1]), self.slider.value(),
                                    self.slider.value())
            self.update()
        except:
            pass

    def go_back(self):
        print(os.path.exists('sources\\' + self.image_list[self.index].split('\\')[-1] + ' @ Ctrl_Z.png'))
        if os.path.exists('sources\\' + self.image_list[self.index].split('\\')[-1] + ' @ Ctrl_Z.png'):
            im = Image.open('sources\\' + self.image_list[self.index].split('\\')[-1] + ' @ Ctrl_Z.png')
            im.save(self.image_list[self.index])

    def vignet(self):
        self.make_vignet.hide()
        self.fu_go_back.hide()
        self.area.show()
        self.ok.show()
        self.opacity.show()
        self.color.show()
        self.area_label.show()
        self.opacity_label.show()
        self.color_label.show()

    def get_vignet_area(self):
        try:
            self.area_val = float(self.area.text())
            self.make_vig()
            self.ok.hide()
            self.area.hide()
            self.opacity.hide()
            self.color.hide()
            self.area_label.hide()
            self.opacity_label.hide()
            self.color_label.hide()
            self.fu_go_back.show()
            self.make_vignet.show()
        except:
            self.area_label.hide()
            self.opacity_label.hide()
            self.color_label.hide()
            self.ok.hide()
            self.area.hide()
            self.opacity.hide()
            self.color.hide()
            self.fu_go_back.show()
            self.make_vignet.show()

    def make_vig(self):
        opacity = float(self.opacity.text())
        red, g, b = int(self.color.text().split()[0]), int(self.color.text().split()[1]), int(
            self.color.text().split()[2])
        print(red, g, b)
        im = Image.open(self.image_list[self.index])
        im.save('sources\\' + self.image_list[self.index].split('\\')[-1] + ' @ Ctrl_Z.png')
        im.close()
        im = Image.open(self.image_list[self.index])
        w, h = im.size
        vign_im = Image.new('RGBA', (w, h), color=(255, 255, 255, 0))
        vign_pix = vign_im.load()
        pixs = im.load()
        area = w * h
        vignet_area = area * self.area_val / 100
        not_vignet_area = area - vignet_area
        r = int(sqrt(not_vignet_area / pi))
        center_x = w // 2
        center_y = h // 2
        for x in range(w):
            for y in range(h):
                distance = int(sqrt((x - center_x) ** 2 + (y - center_y) ** 2))
                if distance > r:
                    change = (distance - r) / int(sqrt(center_x ** 2 + center_y ** 2))
                    vign_pix[x, y] = (red, g, b, int(1000 * change * opacity))
        vign_im.save('vigs/sec.png')
        background = Image.open(self.image_list[self.index])
        foreground = Image.open("vigs/sec.png")

        background.paste(foreground, (0, 0), foreground)
        background.save(self.image_list[self.index])
        self.label_photo.setPixmap(self.file)
        im.close()
        background.close()
        foreground.close()
        print('done')

    def show_ph(self):
        self.way = self.input.text()
        self.file = QPixmap(self.way)
        self.label_photo.setPixmap(self.file)
        if '/' not in self.way and "\\" not in self.way:
            folder = os.getcwd()
            for currentdir, dirs, files in os.walk(folder):
                files_1 = files
                break
        elif '/' in self.way:
            try:
                fl = open(self.way, 'r')
                fl.close()
                folder = '/'.join(self.way.split('/')[:-1])
            except:
                folder = self.way
            for currentdir, dirs, files in os.walk(folder):
                files_1 = files
                break

        elif '\\' in self.way:
            try:
                fl = open(self.way, 'r')
                fl.close()
                folder = '\\'.join(self.way.split('\\')[:-1])
            except:
                folder = self.way
            for currentdir, dirs, files in os.walk(folder):
                files_1 = files
                break

        else:
            folder = os.getcwd()
            for currentdir, dirs, files in os.walk(folder):
                files_1 = files
                break
        self.image_list = []
        self.names = []
        try:
            for file in files_1:
                extension = os.path.splitext(file)[1]
                if extension == '.png' or extension == '.jpg':
                    print(file)
                    self.names.append(file)
                    self.image_list.append(folder + '\\' + file)
        except UnboundLocalError: pass
        try:
            self.index = self.image_list.index(self.way)
        except:
            self.index = 0
        print(self.image_list)
        try:
            im = Image.open(self.image_list[self.index])
            h = self.height()
            w = self.width()
            im_h = im.size[1]
            im_w = im.size[0]
            scale_coef = (h - 170) / im_h
            im_h = h - 170
            im_w *= scale_coef
            if im_w > (w - 25):
                scale_coef = (w - 25) / im_w
                im_w = (w - 25)
                im_h *= scale_coef
            print(self.index)
            self.file = QPixmap(self.image_list[self.index])
            self.file = self.file.scaled(int(im_w), int(im_h))
            self.label_photo.setPixmap(self.file)
            self.info_label.setText(str(im.size)+' '+self.names[self.index])
        except IndexError: pass

    def next(self):

        if len(self.image_list) != 0:
            if len(self.image_list) - self.index > 1:
                self.index += 1
            else:
                self.index = 0
            im = Image.open(self.image_list[self.index])
            h = self.height()
            w = self.width()
            im_h = im.size[1]
            im_w = im.size[0]
            scale_coef = (h - 170) / im_h
            im_h = h - 170
            im_w *= scale_coef
            if im_w > (w - 25):
                scale_coef = (w - 25) / im_w
                im_w = (w - 25)
                im_h *= scale_coef
            self.im_w = im_w
            self.im_h = im_h
            self.file = QPixmap(self.image_list[self.index])
            self.file = self.file.scaled(int(im_w), int(im_h))
            self.label_photo.setPixmap(self.file)
            self.info_label.setText(str(im.size) + ' ' + self.names[self.index])

    def previous(self):

        if len(self.image_list) != 0:
            if abs(self.index)-1 - len(self.image_list) <= -2:
                self.index -= 1
            else:
                self.index = 0
            im = Image.open(self.image_list[self.index])
            h = self.height()
            w = self.width()
            im_h = im.size[1]
            im_w = im.size[0]
            scale_coef = (h - 170) / im_h
            im_h = h - 170
            im_w *= scale_coef
            if im_w > (w - 25):
                scale_coef = (w - 25) / im_w
                im_w = (w - 25)
                im_h *= scale_coef
            self.file = QPixmap(self.image_list[self.index])
            self.file = self.file.scaled(int(im_w), int(im_h))
            self.label_photo.setPixmap(self.file)
            self.info_label.setText(str(im.size) + ' ' + self.names[self.index])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = Win()
    sys.exit(app.exec_())