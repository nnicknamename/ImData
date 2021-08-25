from PyQt5 import QtWidgets, uic, QtCore
from PyQt5 import QtGui
from Box import *
from Preview import *
from Image import *
from Data_stack import *
import cv2

class Boxes_changed(QtCore.QObject):
    boxes_changed = QtCore.pyqtSignal()

class Editor(QtWidgets.QGraphicsScene):
    def __init__(self,data_stack,preview,parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.preview=preview
        self.data_stack=data_stack
        self.lastX=0
        self.lastY=0
        self.scale=1.
        self.changed=QtCore.pyqtSignal()
        self.sig =Boxes_changed()
    def mousePressEvent(self, event): 
        if self.image_selected():
            x,y=self.scale_mouse_position(event.scenePos().x(),event.scenePos().y())
            #sets selected box (if no box is under the mouse selected=None)
            self.get_Image_rep().pick_box_at(x,y)
            self.repaint()

    def mouseMoveEvent(self, event):
        if self.image_selected():
            x,y=self.scale_mouse_position(event.scenePos().x(),event.scenePos().y())
            selectedBox=self.get_Image_rep().get_picked_box()
            if selectedBox:
                selectedBox.move(x-self.lastX,y-self.lastY)
                self.repaint()
            self.lastX=int(x)
            self.lastY=int(y)

    def mouseReleaseEvent(self, event):
        if self.image_selected():
            self.get_Image_rep().unpick_box()

    def keyPressEvent(self, event):
        if(event.modifiers()==QtCore.Qt.ControlModifier and event.key()==QtCore.Qt.Key_Equal):
            self.zoom(1)
            self.repaint()
        elif(event.modifiers()==QtCore.Qt.ControlModifier and event.key()==QtCore.Qt.Key_Minus):
            self.zoom(-1)
            self.repaint()
        elif(event.key()==QtCore.Qt.Key_Backspace):
            self.get_Image_rep().delete_selected_box()
            self.repaint()
            self.sig.boxes_changed.emit()  

    def zoom(self,val):
        if val==1:
            if self.scale+0.1 >0 and self.scale+0.1<=1:
                self.scale+=0.1
        elif val==-1:
            if self.scale-0.1 >0 and self.scale-0.1<=1:
                self.scale-=0.1
        self.scale=round(self.scale,1)

    def add_box(self,x,y):
        self.get_Image_rep().add_box(x,y)
        self.repaint()

    def show_image(self):
        self.qimage =self.get_Image_rep().get_image_with_boxes(self.scale)
        #self.qimage = QtGui.QImage(image.data,image.shape[1]-1, image.shape[0]-1, QtGui.QImage.Format_RGB888).rgbSwapped()
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
    def scale_mouse_position(self,x,y):
        return x/self.scale,y/self.scale

    def set_data_stack(self,data_stack):
        self.data_stack=data_stack