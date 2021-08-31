from Image import *
from PyQt5 import QtWidgets, QtCore

class Batch:
    def __init__(self,name):
        self.name=name
        self.image_reps=list()
        self.selectedImageRep=None

    def add_image_rep(self,image_rep):
        self.image_reps.append(image_rep)
    
    def get_nb_images(self):
        return len(self.image_reps)

    def set_selected_image(self,image_rep):
        if self.selectedImageRep is not None:
            self.selectedImageRep.free_image()
        self.selectedImageRep=image_rep

    def get_selected_image(self):
        return self.selectedImageRep

    def get_tree(self):
        Bitem = QtWidgets.QTreeWidgetItem([self.name])
        Bitem.setData(0, QtCore.Qt.UserRole,"Batch")
        for i in self.image_reps: 
            item=QtWidgets.QTreeWidgetItem([i.get_name(),str(i.get_nb_boxes())])
            item.setData(0, QtCore.Qt.UserRole,"image")
            Bitem.addChild(item)
        return Bitem

    def get_name(self):
        return self.name

    def is_image_in_Batch(self,image_file):
        for i in self.image_reps:
            if i.get_name== image_file:
                return True
        return False        
        
    def select_image_with_file(self,image_file):
        print("image sselected")
        for i in self.image_reps:
            if i.get_name()== image_file:
                self.set_selected_image(i)
                return 0

    def get_images(self):
        return self.image_reps

    def delete_image(self,file_name):
        for i in self.image_reps:
            if i.get_name()==file_name:
                self.image_reps.remove(i)
                return 1
        return 0
    
    