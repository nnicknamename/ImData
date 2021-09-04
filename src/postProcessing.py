from PyQt5 import QtWidgets, uic ,QtCore
from Data_stack import *
from renderer import *
from processor import *
import cv2
class postProcessing(QtWidgets.QWidget):

    def __init__(self,data_stack=None,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        uic.loadUi('src/ui/postProcessing.ui', self) 
        self.data_stack=data_stack
        self.proc=processor()

    def set_data_stack(self,data_stack):
        self.data_stack=data_stack

    def chooseExportFile(self):
        options = QtWidgets.QFileDialog.Options()
        fileName ,_= QtWidgets.QFileDialog.getOpenFileName()(self,"QFileDialog.getOpenFileNames()", "","stack files (*.)", options=options)
        self.exportPath.setText(fileName)

    def export(self):
        #get params from the fields 
        #init renderer 
        #and generate 
        gen=renderer(self.data_stack,processor(self.widthField.value(),self.heightField.value(),self.interpolationCombo.itemData(self.interpolationCombo.currentIndex()), None))
        data,classes=gen.get_as_numpy_array(self.data_stack.get_rep())
        gen.save_dataset(data,classes)
    