from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.open_win()

    def open_win(self):
        self.setGeometry(400,100,720,720)
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

        self.next_photo = QPushButton('Next',self)
        self.next_photo.move(420,680)

        self.previous_photo = QPushButton('Previous',self)
        self.previous_photo.move(220,680)

        self.bottom_control.addWidget(self.next_photo)
        self.bottom_control.addWidget(self.previous_photo)

        file = QPixmap('E:/Sources/Photoshop/cartoon/1_1.png') # путь
        lbl = QLabel(self)
        lbl.setPixmap(file)
        lbl.move(500,500)

        self.photo_area.addWidget(lbl)

        self.main_layout.addLayout(self.photo_area)
        self.main_layout.addLayout(self.bottom_control)

        return self.main_layout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = Win()
    sys.exit(app.exec_())