import numpy as np
import cv2
class renderer:
    def __init__(self,data_stack):
        self.data_stack=data_stack
        
    def get_as_numpy_array(self):
        arr=list()
        classes=list()
        Batches=self.data_stack.get_batches()
        nb_batches=self.data_stack.get_nb_batches()
        k=0
        for b in Batches:
            images= b.get_images()  
            for i in images:
                boxes=i.get_boxes()
                for bx in boxes:
                    a=[0 for n in range(nb_batches)]
                    a[k]=1
                    classes.append(a)
                    image=i.get_image()[bx.y:bx.y+bx.height, bx.x:bx.x+bx.width]
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    arr.append(gray)
            k+=1

        return classes , np.array(arr)


    def save_dataset(self,images,classes):
        np.savez("dataset", images,classes)

    def save_as_torch_dataset(self):
        pass 
        