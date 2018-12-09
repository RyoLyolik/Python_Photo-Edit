from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import PyQt5.QtCore
from PIL import Image

class Vignet(QMainWindow):
    def __init__(self, image):
        super().__init__()
        self.index = 0

        self.open_win()

    def open_win(self):
        self.setGeometry(400, 100, 100, 100)
        self.setWindowTitle('Title')
        control = self.vignet_settings()
        main_widg = QWidget()
        main_widg.setLayout(control)
        self.setCentralWidget(main_widg)

        self.show()

    def vignet_settings(self):

