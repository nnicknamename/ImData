class Box:

    def __init__(self,x,y,width,height,image_width,image_height,name):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.image_width=image_width
        self.image_height=image_height
        self.name=name
        self.select_mode=[0,0,0,0]
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

    def set_selct_mode(self,posX,posY):
        self.select_mode=[0,0,0,0]
        if posX>self.x+self.width-5:
            self.select_mode[2]=1
        elif posX<self.x+5:
            self.select_mode[0]=1

        if posY>self.y+self.height-5:
            self.select_mode[3]=1
        elif posY<self.y+5:
            self.select_mode[1]=1

    def edit(self,posX,posY,x,y):
        if (self.select_mode==[0,0,0,0]):
            self.set_position(self.x+x, self.y+y)
        else:
            if self.select_mode[2]==1:
                self.width+=int(x)
                self.height+=int(x)
            if self.select_mode[3]==1:
                self.height+=int(y)
                self.width+=int(y)
        
        return 0
    def is_inside(self, x,y):
        return ( x>self.x and y>self.y and x<self.x+self.width and y<self.y+self.height )

    def get_name(self):
        return str(self.name)

    def set_name(self,name):
        self.name=name