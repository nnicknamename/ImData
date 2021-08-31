from PyQt5 import QtWidgets,QtGui
import cv2

class Preview(QtWidgets.QGraphicsScene):
    def __init__(self,parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)

    def set_image(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytesPerLine = ch * w
        img= QtGui.QImage(img.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.image=img
        self.paint()

    def show_image(self):
        self.qimage = self.image
        self.pixmap=QtGui.QPixmap.fromImage(self.qimage)
        self.item =QtWidgets.QGraphicsPixmapItem(self.pixmap)
        self.clear()
        self.addItem(self.item)
        self.update()

    def paint(self):
        self.show_image()
