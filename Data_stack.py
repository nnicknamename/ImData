
from Batch import *
from Image import *
class Data_stack:
    def __init__(self):
        self.batches=list()
        self.selectedBatch=None

    def add_batch(self,batch):
        self.batches.append(batch)

    def select_batch(self,batch):
        self.selectedBatch=batch

    def select_batch_with_name(self,name):
        for b in self.batches:
            if b.get_name() == name:
                print("batch found")
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

    