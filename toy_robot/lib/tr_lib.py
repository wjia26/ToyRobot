"""
Defines the Robot and Table classes required for __main__.py
Author: William Jiang
"""

class Table:
    """
    A class used to represent a Tabletop.

    Attributes:
    -----------
    x_dim: int
        Number of units of the x dimension
    y_dim: int
        Number of units of the y dimension

    Methods
    -------
    get_dim():
        Returns the dimensions of the table in the form x_dim,y_dim
    """
    def __init__(self,x,y):
        self.x_dim=x
        self.y_dim=y
    def get_dim(self):
        return self.x_dim,self.y_dim
        
class Robot:

    def __init__(self):   
        self.x,self.y,self.f=None,None,None
        self.on_table=False
        #store all directions as an array
        self.f_arr=["EAST","NORTH","WEST","SOUTH"]

    def place(self,x_in,y_in,f_in,table_obj):       
        x_dim,y_dim=table_obj.get_dim()
        if x_in>x_dim or y_in>y_dim:
            print("You can't place the robot there")
        else:
            self.x,self.y,self.f=x_in,y_in,f_in
            self.on_table=True
        
        return [self.x,self.y,self.f]
    def move(self,table_obj):
        x_dim,y_dim=table_obj.get_dim()
        if self.f=="NORTH":
            if self.y==y_dim:
                pass
            else:
                self.y+=1
        elif self.f=="EAST":
            if self.x==x_dim:
                pass
            else:
                self.x+=1
        elif self.f=="WEST":
            if self.x==0:
                pass
            else:
                self.x-=1
        elif self.f=="SOUTH":
            if self.x==0:
                pass
            else:
                self.y-=1
        else:
            raise ValueError

        return [self.x,self.y,self.f]

    def left(self):
        next_ind=self.f_arr.index(self.f)+1
        if next_ind>3:
            next_ind=0
        else:
            next_ind
        self.f=self.f_arr[next_ind]
        #Take the value of the next index
        return [self.x,self.y,self.f]
            
    def right(self):)
        next_ind=self.f_arr.index(self.f)-1
        if next_ind<0:
            next_ind=3
        else:
            next_ind
        #Take the value of the next index
        self.f=self.f_arr[next_ind]

        return [self.x,self.y,self.f]

    def report(self):      
        return [self.x,self.y,self.f]
    def is_on_table(self):

        return self.on_table
    
    def reset(self):
   
        self.x,self.y,self.f=None,None,None
        self.on_table=False
        return [self.x,self.y,self.f]
    

