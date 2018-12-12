import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QMouseEvent, QImage, QPixmap
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()
    def initUI(self):



        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255,255,255))
        self.resize(500, 500)
        self.file = QPixmap('E:/Sources/Photoshop/cartoon/1_1.png')  # путь
        self.label_ph = QLabel(self)
        self.label_ph.setPixmap(self.file)
        self.show()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.flag = True
            self.paint = QPainter(self.image)
            self.ellips(e)
    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0,0, self.image)
    def mouseMoveEvent(self, e):
        if self.flag:
            print(e.pos())
            self.ellips(e)
    def ellips(self,e):
        self.paint.setBrush(QColor('black'))
        self.paint.drawEllipse(e.pos(), 10,10)
        self.update()
app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())