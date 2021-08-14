from PyQt5 import QtWidgets
from Box import *
import cv2

class Image :
    "Image class represents an image including its Boxes"
    def __init__(self,image_file):
        self.image_file=image_file
        self.image=cv2.imread(self.image_file)
        self.boxes=list()
        self.selectedBox=None

    def add_box(self,x,y):
        self.boxes.insert(0,Box(x,y,100,100,self.image.shape[1], self.image.shape[0],self.get_nb_boxes()+1))

    def get_box_at(self,x,y):
        for b in self.boxes:
            if b.is_inside(x,y) :
                return b
        return None

    def get_image(self):
        return self.image

    def get_image_with_boxes(self):
        Cimage = self.image.copy()
        for b in self.boxes:
            if b == self.selectedBox:
                ch = cv2.addWeighted(Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:],0.8,0,1-0.5,0)
                Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:] = ch
            else:
                ch = cv2.addWeighted(Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:],0.5,0,1-0.5,0)
                Cimage[b.y:b.y+b.height,b.x:b.x+b.width,:] = ch
        return Cimage

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

    def delete_box(sef,name):
        for b in self.boxes:
            if b.get_name() == name:
                self.boxes.remove(b)            
                return 1
    