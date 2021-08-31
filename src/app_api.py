from Editor import *
from Preview import *
from Image import *
from Data_stack import *
from Batch import *
import pickle

class app_api:
    def __init__(self,data_stack,batch_tree,boxes_tree,preview,graphicsView):
        self.previewScene=Preview(preview)
        self.data_stack=data_stack
        self.editor=Editor(self.data_stack,self.previewScene,graphicsView)
        graphicsView.setScene(self.editor)
        preview.setScene(self.previewScene)
        self.batch_tree=batch_tree
        self.batch_tree.insertTopLevelItems(0,self.data_stack.get_tree_list())
        self.boxes_tree=boxes_tree
        self.editor.sig.boxes_changed.connect(self.update_boxes_tree)
        self.editor.sig.boxes_changed.connect(self.update_batch_tree)

    
    def select_image(self,name):
        self.data_stack.get_selected_batch().select_image_with_file(name)
        self.update_boxes_tree()
        self.editor.paint()

    def select_batch(self,name):
        self.data_stack.select_batch_with_name(name)
        self.update_boxes_tree()

    def add_batch(self,name):
        batch=Batch(name)
        self.data_stack.add_batch(batch)
        self.update_batch_tree()

    def add_image(self,image_file):
        image=Image(image_file)
        self.data_stack.get_selected_batch().add_image_rep(image)
        self.update_batch_tree()

    def add_box(self,x,y):
        self.editor.add_box(x,y)
        self.update_boxes_tree()

    def slect_box(self,name):
        self.data_stack.get_selected_batch().get_selected_image().select_box(name)
        self.editor.manage_preview()
        self.editor.repaint()
        self.data_stack.get_selected_batch().get_selected_image().selectedBox=None

    def update_batch_tree(self):
        self.batch_tree.clear()
        self.batch_tree.insertTopLevelItems(0,self.data_stack.get_tree_list())
        self.batch_tree.update()

    def update_boxes_tree(self):
        self.boxes_tree.clear()
        if self.data_stack.get_selected_batch() and self.data_stack.get_selected_batch().get_selected_image():
            self.boxes_tree.insertTopLevelItems(0,self.data_stack.get_selected_batch().get_selected_image().get_Boxes_tree())
        self.batch_tree.update()

    def save(self,path):
        rep=self.data_stack.get_rep()
        with open(path,'wb') as fil:
            pickle.dump(rep,fil)

    def load(self,path):
        fil=open(path,'rb')
        self.data_stack=Data_stack(pickle.load(fil))
        self.update_boxes_tree()
        self.update_batch_tree()
        self.editor.set_data_stack(self.data_stack)
        self.editor.paint()

    def get_data_stack(self):
        return self.data_stack