from PyQt5 import QtWidgets
from PyQt5 import QtGui
from Box import *
import cv2

class Image :
    """
    Image class represents an image including its Boxes
    """
    def __init__(self,image_file):
        self.image_file=image_file
        self.loaded=False
        self.boxes=list()
        self.selectedBox=None
        self.pickedBox=None

    def add_box(self,x,y):
        self.boxes.insert(0,Box(x,y,400,400,self.image.shape[1], self.image.shape[0],self.get_nb_boxes()+1))

    def get_box_at(self,x,y):
        for b in self.boxes:
            if b.is_inside(x,y) :
                return b
        return None

    def get_image(self):
        if not self.loaded:
            self.image=cv2.imread(self.image_file)
            self.loaded=True
        return self.image

    def free_image(self):
        self.image=None
        self.loaded=False
    def get_image_with_boxes(self,scale):
        Cimage = self.get_image().copy()
        for b in self.boxes:
            if b == self.selectedBox:
                ch = cv2.addWeighted(Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:],0.8,0,0.5,0)
                Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:] = ch
            else:
                ch = cv2.addWeighted(Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:],0.5,0,0.5,0)
                Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:] = ch
        Cimage=cv2.resize(Cimage,None,fx=scale, fy=scale, interpolation = cv2.INTER_LINEAR)
        Cimage = cv2.cvtColor(Cimage, cv2.COLOR_BGR2RGB)
        h, w, ch = Cimage.shape
        bytesPerLine = ch * w
        return QtGui.QImage(Cimage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
         

    def select_box_at(self,x,y):
        for b in self.boxes:
            if b.is_inside(x,y) :
                self.selectedBox=b
                return 0
        self.selectedBox=None

    def get_selected_box(self):
        return self.selectedBox

    def set_selected_box(self,box):
        self.selectedBox=box

    def get_nb_boxes(self):
        return len(self.boxes)

    def get_name(self):
        return self.image_file

    def get_Boxes_tree(self):
        boxes=[]
        for b in self.boxes:
            boxes.insert(0,QtWidgets.QTreeWidgetItem([str(b.get_name())]))
        return boxes

    def select_box(self,name):
        for b in self.boxes:
            if b.get_name() == name:
                self.selectedBox=b            
                return 1

    def get_boxes(self):
        return self.boxes

    def set_boxes(self,boxes):
        self.boxes=boxes

    def delete_box(self,name):
        for b in self.boxes:
            if b.get_name() == name:
                self.boxes.remove(b)            
                return 1
        self.update_box_names()

    def update_box_names(self):
        k=self.get_nb_boxes()
        for b in self.boxes:
            b.set_name(str(k))
            k-=1
        print("updated")
    def delete_selected_box(self):
        self.delete_box(self.selectedBox.get_name())            
        self.update_box_names()
    def pick_box_at(self,x,y):
        """
            picking a box selects it too 
            used to move boxes in editor
        """
        self.select_box_at(x,y)
        self.pickedBox=self.selectedBox

    def unpick_box(self):
        self.pickedBox=None

    def get_picked_box(self):
        return self.pickedBox