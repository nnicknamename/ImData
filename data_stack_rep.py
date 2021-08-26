class data_stack_rep:
    def __init__(self,data_stack):
        self.stack={}
        for b in data_stack.get_batches():
            self.stack[b.get_name()]={}
            for i in b.get_images():
                self.stack[b.get_name()][i.get_name()]=i.get_boxes()
    def get_rep(self):
        return self.stack