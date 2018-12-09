from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
from PIL import Image
from math import pi, sqrt
from PyQt5.QtCore import *


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

        self.buaty_lbl = QLabel('', self)
        self.buaty_lbl2 = QLabel('', self)
        self.buaty_lbl.setFixedSize(200, 1)
        self.buaty_lbl2.setFixedSize(100, 1)

        self.zoom = QSlider()
        self.zoom.setOrientation(Qt.Horizontal)
        self.zoom.setMaximum(1000)
        self.zoom.setMinimum(0)
        self.zoom.valueChanged.connect(self.zooming)
        self.zoom_lbl = QLabel('100%')


        self.bottom_control.addWidget(self.buaty_lbl)
        self.bottom_control.addWidget(self.previous_photo)
        self.bottom_control.addWidget(self.next_photo)
        self.bottom_control.addWidget(self.buaty_lbl2)
        self.bottom_control.addWidget(self.zoom)
        self.bottom_control.addWidget(self.zoom_lbl)

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

        self.area_lbl = QLabel('area, %', self)
        self.opacity_lbl = QLabel('opacity, [0;1]', self)
        self.color_lbl = QLabel('color, RGB', self)

        self.area_lbl.hide()
        self.opacity_lbl.hide()
        self.color_lbl.hide()

        self.make_vignet = QPushButton('Виньетка', self)
        self.make_vignet.setFixedSize(60, 20)
        self.make_vignet.clicked.connect(self.vignet)
        self.fu_go_back = QPushButton('Cancel', self)
        self.fu_go_back.setFixedSize(60, 20)
        self.fu_go_back.clicked.connect(self.go_back)

        self.edit_photo_control.addWidget(self.area)
        self.edit_photo_control.addWidget(self.area_lbl)
        self.edit_photo_control.addWidget(self.opacity)
        self.edit_photo_control.addWidget(self.opacity_lbl)
        self.edit_photo_control.addWidget(self.color)
        self.edit_photo_control.addWidget(self.color_lbl)
        self.edit_photo_control.addWidget(self.fu_go_back)
        self.edit_photo_control.addWidget(self.make_vignet)
        self.edit_photo_control.addWidget(self.ok)

        self.photo_scroll = QScrollArea()
        self.file = QPixmap('E:/Sources/Photoshop/cartoon/1_1.png')  # путь
        self.lbl_ph = QLabel(self)
        self.lbl_ph.setPixmap(self.file)
        self.photo_scroll.setWidget(self.lbl_ph)
        # self.lbl_ph.move(5000, 5000)

        self.photo_area.addWidget(self.photo_scroll)

        self.main_layout.addLayout(self.top_control)
        self.main_layout.addLayout(self.edit_photo_control)
        self.main_layout.addLayout(self.photo_area)
        self.main_layout.addLayout(self.bottom_control)

        return self.main_layout

    def zooming(self):
        image = Image.open(self.image_list[self.index])
        w, h = image.size

        image.close()
        size = self.zoom.value() / 100
        print((w*size) + 100, (h*size) + 100)

        self.zoom_lbl.setText(str(size) + '%')
        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(w*size, h*size)
        self.lbl_ph.setPixmap(self.file)
        self.resize((w * size) + 100, (h * size) + 100)
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
        self.area_lbl.show()
        self.opacity_lbl.show()
        self.color_lbl.show()

    def get_vignet_area(self):
        try:
            self.area_val = float(self.area.text())
            self.make_vig()
            self.ok.hide()
            self.area.hide()
            self.opacity.hide()
            self.color.hide()
            self.area_lbl.hide()
            self.opacity_lbl.hide()
            self.color_lbl.hide()
            self.fu_go_back.show()
            self.make_vignet.show()
        except:
            self.area_lbl.hide()
            self.opacity_lbl.hide()
            self.color_lbl.hide()
            self.ok.hide()
            self.area.hide()
            self.opacity.hide()
            self.color.hide()
            self.fu_go_back.show()
            self.make_vignet.show()

    def make_vig(self):
        opacity = float(self.opacity.text())
        r, g, b = int(self.color.text().split()[0]), int(self.color.text().split()[1]), int(
            self.color.text().split()[2])
        print(r, g, b)
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
                    vign_pix[x, y] = r, g, b, int(1000 * change * opacity)
        vign_im.save('vigs/sec.png')
        background = Image.open(self.image_list[self.index])
        foreground = Image.open("vigs/sec.png")

        background.paste(foreground, (0, 0), foreground)
        background.save(self.image_list[self.index])
        self.lbl_ph.setPixmap(self.file)
        im.close()
        background.close()
        foreground.close()
        print('done')

    def show_ph(self):
        self.way = self.input.text()
        self.file = QPixmap(self.way)
        self.lbl_ph.setPixmap(self.file)
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

        for file in files_1:
            extension = os.path.splitext(file)[1]
            if extension == '.png' or extension == '.jpg':
                print(file)
                self.image_list.append(folder + '\\' + file)
        try:
            self.index = self.image_list.index(str(folder) + '\\' + str(self.way))
        except:
            self.index = 0
        print(self.image_list)
        self.next()
        self.previous()

    def next(self):
        if len(self.image_list) - self.index > 1:
            self.index += 1
        else:
            self.index = 0
        im = Image.open(self.image_list[self.index])
        h = self.height()
        w = self.width()
        im_h = im.size[1]
        im_w = im.size[0]
        scale_coef = (h - 135) / im_h
        im_h = h - 135
        im_w *= scale_coef
        if im_w > (w - 25):
            scale_coef = (w - 25) / im_w
            im_w = (w - 25)
            im_h *= scale_coef
        self.im_w = im_w
        self.im_h = im_h
        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(int(im_w), int(im_h))
        self.lbl_ph.setPixmap(self.file)

    def previous(self):
        if abs(self.index) - len(self.image_list) <= -1:
            self.index -= 1
        else:
            self.index = 0
        im = Image.open(self.image_list[self.index])
        h = self.height()
        w = self.width()

        im_h = im.size[1]
        im_w = im.size[0]
        scale_coef = (h - 135) / im_h
        im_h = h - 135
        im_w *= scale_coef
        if im_w > (w - 25):
            scale_coef = (w - 25) / im_w
            im_w = (w - 25)
            im_h *= scale_coef
        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(int(im_w), int(im_h))
        self.lbl_ph.setPixmap(self.file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = Win()
    sys.exit(app.exec_())
