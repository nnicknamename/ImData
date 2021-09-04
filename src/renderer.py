import numpy as np
from Image import *
import cv2
class renderer:
    def __init__(self,data_stack,processor):
        self.data_stack=data_stack
        self.processor=processor
        
    def get_as_numpy_array(self,rep):
        arr=list()
        classes=list()
        k=0
        for batch_name in rep:
            for image_path in rep[batch_name]:
                for bx in rep[batch_name][image_path]:
                    a=[0 for n in range(len(rep))]
                    a[k]=1
                    classes.append(a)
                    image=Image(image_path)
                    boxedImage=image.get_image()[bx.y:bx.y+bx.height, bx.x:bx.x+bx.width]
                    boxedImage=self.processor.processImage(boxedImage)
                    gray = cv2.cvtColor(boxedImage, cv2.COLOR_BGR2GRAY)
                    #process image
                    arr.append(gray)
            k+=1
        return classes , np.array(arr)

    def save_dataset(self,images,classes):
        np.savez("dataset", images,classes)

    def save_as_torch_dataset(self):
        pass 
        