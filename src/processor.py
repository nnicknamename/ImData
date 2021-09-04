import cv2

class processor:
    validnter={"Area":cv2.INTER_AREA,"Cubic":cv2.INTER_CUBIC,"Linear":cv2.INTER_LINEAR}
    def __init__(self,width=0,height=0,interpolation=None,reg=None):
        self.width=width
        self.height=height
        if interpolation is not None:
            self.interpolation=processor.validnter[interpolation]
        else:
            self.interpolation=None
        self.reg=reg

    def processImage(self,image):
        return cv2.resize(image,(self.width,self.height),interpolation=self.interpolation)

    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height

    def set_interp(self,interpolation):
        self.interpolation=processor.validnter[interpolation]

    def set_reg(self,reg):
        self.reg=reg