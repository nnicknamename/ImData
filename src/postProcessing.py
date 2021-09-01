from PyQt5 import QtWidgets, uic ,QtCore
from Data_stack import *
from renderer import *

class postProcessing(QtWidgets.QWidget):

    def __init__(self,data_stack=None,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        uic.loadUi('src/ui/postProcessing.ui', self) 
        self.data_stack=data_stack

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
        gen=renderer(self.data_stack)
        data,classes=gen.get_as_numpy_array()
        gen.save_dataset(data,classes)