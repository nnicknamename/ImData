

class Box:
    def __init__(self,x,y,width,height,image_width,image_height,name):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.image_width=image_width
        self.image_height=image_height
        self.name=name
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def set_position(self,x,y):
        if x>=0 and x+self.width<self.image_width: 
            self.x=int(x)
        elif x+self.width>=self.image_width:
            self.x=self.image_width-self.width
        
        if y>=0 and y+self.height<self.image_height:
            self.y=int(y)
        elif y+self.height>=self.image_height:
            self.y=self.image_height-self.height

    
    def move(self,x,y):
        self.set_position(self.x+x, self.y+y)

    def is_inside(self, x,y):
        return ( x>self.x and y>self.y and x<self.x+self.width and y<self.y+self.height )

    def get_name(self):
        return str(self.name)

    def set_name(self,name):
        self.name=name