from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import PyQt5.QtCore
from PIL import Image


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_list = []
        self.index = 0

        self.open_win()

    def open_win(self):
        self.setGeometry(400, 100, 720, 720)
        self.setWindowTitle('Title')
        control = self.contr()
        main_widg = QWidget()
        main_widg.setLayout(control)
        self.setCentralWidget(main_widg)

        self.show()

    def contr(self):
        self.main_layout = QVBoxLayout()
        self.bottom_control = QHBoxLayout()
        self.photo_area = QVBoxLayout()
        self.top_control = QVBoxLayout()

        self.input = QLineEdit()
        # self.input.setFixedSize(100,25)

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

        self.file = QPixmap('E:/Sources/Photoshop/cartoon/1_1.png')  # путь
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.file)
        self.lbl.move(500, 500)

        self.photo_area.addWidget(self.lbl)

        self.main_layout.addLayout(self.top_control)
        self.main_layout.addLayout(self.photo_area)
        self.main_layout.addLayout(self.bottom_control)

        return self.main_layout

    def show_ph(self):
        self.way = self.input.text()
        self.file = QPixmap(self.way)
        self.lbl.setPixmap(self.file)
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

    def next(self):
        h = self.height()
        w = self.width()
        area = h*w

        if len(self.image_list) - self.index > 1:
            self.index += 1
        else:
            self.index = 0
        im = Image.open(self.image_list[self.index])
        im_h = im.size[0]
        im_w = im.size[1]
        im_area = im_h*im_w
        self.file = QPixmap(self.image_list[self.index])
        self.file = self.file.scaled(int(im_w*(im_area/area)*100),int(im_h*(im_area/area)*100))
        # self.file = self.file.scaled(1,1)
        self.lbl.setPixmap(self.file)

    def previous(self):
        if abs(self.index) - len(self.image_list) < -1:
            self.index -= 1
        else:
            self.index = 0

        print(self.index)
        self.file = QPixmap(self.image_list[self.index])

        self.lbl.setPixmap(self.file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = Win()
    sys.exit(app.exec_())
