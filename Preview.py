from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import cv2

class Preview(QtWidgets.QGraphicsScene):

    def __init__(self,parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)

    def set_image(self,img):
        self.image=img.copy()
        self.paint()

    def show_image(self):
        self.qimage = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap=QtGui.QPixmap.fromImage(self.qimage)
        self.item =QtWidgets.QGraphicsPixmapItem(self.pixmap)
        self.clear()
        self.addItem(self.item)
        self.update()

    def paint(self):
        self.show_image()