
from Batch import *
from Image import *
class Data_stack:
    def __init__(self,rep=None):
        self.batches=list()
        self.selectedBatch=None 
        if rep is not None:
            for batch_name in rep:
                batch=Batch(batch_name)
                for image_path in rep[batch_name]:
                    image=Image(image_path)
                    image.set_boxes(rep[batch_name][image_path])
                    batch.add_image_rep(image)
                self.add_batch(batch)
    def add_batch(self,batch):
        self.batches.append(batch)

    def select_batch(self,batch):
        self.selectedBatch=batch

    def select_batch_with_name(self,name):
        for b in self.batches:
            if b.get_name() == name:
                self.select_batch(b)

    def get_selected_batch(self):
        return self.selectedBatch

    def get_tree_list(self):
        item=[]
        for b in self.batches:
            item.append(b.get_tree())
        return item
    
    def batch_name_exists(self,name):
        for b in self.batches:
            if b.get_name() == name:
                return True
        return False

    def get_batches(self):
        return self.batches

    def get_nb_batches(self):
        return len(self.batches)

    def delete_batch(self,name):
        for b in self.batches:
            if b.get_name()==name:
                self.batches.remove(b)
                return 1
        return 0