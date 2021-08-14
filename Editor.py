from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Box import *
from Preview import *
from Image import *
from Data_stack import *
import cv2

class Editor(QtWidgets.QGraphicsScene):
    def __init__(self,data_stack,preview,parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.preview=preview
        self.data_stack=data_stack
        self.lastX=0
        self.lastY=0

    def mousePressEvent(self, event): 
        if self.image_selected():
            x = event.scenePos().x()
            y = event.scenePos().y()
            self.get_Image_rep().select_box_at(x,y)
            self.repaint()

    def mouseMoveEvent(self, event):
        if self.image_selected():
            x = event.scenePos().x()
            y = event.scenePos().y()
            selectedBox=self.get_Image_rep().get_selected_box()
            if selectedBox:
                selectedBox.move(x-self.lastX,y-self.lastY)
                self.repaint()
            self.lastX=int(x)
            self.lastY=int(y)

    def mouseReleaseEvent(self, event):
        if self.image_selected():
            self.get_Image_rep().set_selected_box(None)

    def add_box(self,x,y):
        self.get_Image_rep().add_box(x,y)
        self.repaint()

    def show_image(self):
        image=self.get_Image_rep().get_image_with_boxes()
        self.qimage = QtGui.QImage(image.data,image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap=QtGui.QPixmap.fromImage(self.qimage)
        self.item =QtWidgets.QGraphicsPixmapItem(self.pixmap)
        self.clear()
        self.addItem(self.item)
        self.update()
        self.manage_preview()

    def manage_preview(self):
        selectedBox=self.get_Image_rep().get_selected_box()
        if selectedBox:
            self.preview.set_image(self.get_Image_rep().get_image()[selectedBox.y:selectedBox.y+selectedBox.height, selectedBox.x:selectedBox.x+selectedBox.width])
            self.preview.paint()
        else:
            self.preview.clear()
            self.preview.update()

    def paint(self):
        if self.image_selected():
            self.show_image()

    def repaint(self):
        if self.image_selected():
            self.show_image()
    
    def get_Image_rep(self):
        if(self.image_selected()):
            return self.data_stack.get_selected_batch().get_selected_image()
        return None

    def image_selected(self):
        if self.data_stack.get_selected_batch() :
            if self.data_stack.get_selected_batch().get_selected_image():
                return True
        return False      