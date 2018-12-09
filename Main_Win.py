from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import PyQt5.QtCore
from PIL import Image
from vignet import Vignet


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
        self.buaty_lbl2.setFixedSize(200, 1)

        self.bottom_control.addWidget(self.buaty_lbl)
        self.bottom_control.addWidget(self.previous_photo)
        self.bottom_control.addWidget(self.next_photo)
        self.bottom_control.addWidget(self.buaty_lbl2)

        self.make_vignet = QPushButton('Виньетка', self)
        self.make_vignet.setFixedSize(60,20)
        self.make_vignet.clicked.connect(self.vignet)


        self.edit_photo_control.addWidget(self.make_vignet)

        self.file = QPixmap('E:/Sources/Photoshop/cartoon/1_1.png')  # путь
        self.lbl_ph = QLabel(self)
        self.lbl_ph.setPixmap(self.file)
        # self.lbl_ph.move(5000, 5000)

        self.photo_area.addWidget(self.lbl_ph)

        self.main_layout.addLayout(self.top_control)
        self.main_layout.addLayout(self.edit_photo_control)
        self.main_layout.addLayout(self.photo_area)
        self.main_layout.addLayout(self.bottom_control)

        return self.main_layout

    def vignet(self):
        im = Image.open(self.image_list[self.index])
        size = im.size
        w = im.size[0]
        h = im.size[1]
        area = w*h

        print(size)

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
        print('\\' in self.way)
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
        scale_coef = (h-135) / im_h
        im_h = h-135
        im_w *= scale_coef
        if im_w > (w-25):
            scale_coef = (w-25) / im_w
            im_w = (w-25)
            im_h *= scale_coef

        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(int(im_w),int(im_h))
        self.lbl_ph.setPixmap(self.file)

    def previous(self):
        if abs(self.index) - len(self.image_list) < -1:
            self.index -= 1
        else:
            self.index = 0

        im = Image.open(self.image_list[self.index])
        h = self.height()
        w = self.width()

        im_h = im.size[1]
        im_w = im.size[0]
        scale_coef = (h-135) / im_h
        im_h = h-135
        im_w *= scale_coef
        if im_w > (w-25):
            scale_coef = (w-25) / im_w
            im_w = (w-25)
            im_h *= scale_coef
        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(int(im_w),int(im_h))
        self.lbl_ph.setPixmap(self.file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = Win()
    sys.exit(app.exec_())
