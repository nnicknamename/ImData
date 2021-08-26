from PyQt5 import QtWidgets, uic ,QtCore
from PyQt5 import QtGui
from Editor import *
from Preview import *
from Image import *
from Data_stack import *
from Batch import *
from Add_batch_dialog import *
from app_api import *
from render import *
import cv2
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self) 
        self.dataStack=Data_stack()
        self.init_Editor()
        self.api=app_api(self.dataStack, self.editor, self.Batch_images_tree, self.Boxes_tree)
        self.show()

    def init_Editor(self):
        self.previewScene=Preview()
        self.editor=Editor(self.dataStack,self.previewScene)
        self.graphicsView.setScene(self.editor)
        self.preview.setScene(self.previewScene)

    def add_image(self):
        options = QtWidgets.QFileDialog.Options()
        fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","Image files (*.jpg *.png)", options=options)
        self.load_images(fileNames)
    def load_images(self,files):
        for f in files:
            if f and not self.api.get_data_stack().get_selected_batch().is_image_in_Batch(f):
                self.api.add_image(f)
            else:
                dlg = QtWidgets.QMessageBox(self)
                dlg.setWindowTitle("Error")
                dlg.setText("this Image is already in the selected Batch")
                exit(0)
    def add_batch(self):
        dialog=Add_batch_dialog(self.dataStack,self)
        self.api.add_batch(dialog.name)

    def add_box(self):
        self.api.add_box(100, 100)

    def select_Image(self,index):
        selected = self.Batch_images_tree.selectedItems()
        if selected:
            item = selected[0]
            if item.data(0, QtCore.Qt.UserRole)=="Batch":
                self.api.select_batch(item.data(0,0))
            elif item.data(0, QtCore.Qt.UserRole)=="image":
                self.api.select_image(item.data(0,0))

    def select_box(self):
        selected = self.Boxes_tree.selectedItems()
        if selected:
            print("test")
            item = selected[0]
            self.api.slect_box(item.data(0,0))
    def generate(self):
        print ("test")
        gen=renderer(self.dataStack)
        data,classes=gen.get_as_numpy_array()
        gen.save_dataset(data,classes)
    def save(self):
        options = QtWidgets.QFileDialog.Options()
        fileName ,_= QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getOpenFileNames()", "","Image files (*.stk)", options=options)
        
        self.api.save(fileName)

    def load(self):
        options = QtWidgets.QFileDialog.Options()
        fileName ,_= QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileNames()", "","stack files (*.stk)", options=options)
        self.api.load(fileName)
        #self.dataStack=self.api.get_data_stack()
        #self.init_Editor()
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()