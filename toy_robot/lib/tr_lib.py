"""
Defines the Robot and Table classes required for __main__.py
Author: William Jiang
"""

class Table:

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

    def cmd(self,line,table_obj):
   
        arr_cmd=line.split()
        command=arr_cmd[0]
        if(command=='PLACE'):
            arr_in=arr_cmd[1].split(",") 
            self.place(int(arr_in[0]),int(arr_in[1]),arr_in[2],table_obj)
        elif(self.is_on_table()):
            if(command=='MOVE'):
                self.move(table_obj)
            elif (command=='LEFT'):
                self.left()
            elif (command=='RIGHT'):
                self.right()
            elif (command=='REPORT'):
                self.report()

        return [self.x,self.y,self.f]
        
    def place(self,x_in,y_in,f_in,table_obj):
        """
        Places the robot on the tabletop with coordinates and an orientation.

        Parameters
        ----------
        x_in: int
            Input for the x coordinate of where to place the robot.
        y_in: int
            Input for the y coordinate of where to place the robot.
        f_in: string
            Input for the orientation, f.
        table_obj: Table.Object
            Tabletop object of class Table.

        """        
        x_dim,y_dim=table_obj.get_dim()
        if x_in>x_dim or y_in>y_dim:
            print("You can't place the robot there")
        else:
            self.x,self.y,self.f=x_in,y_in,f_in
            self.on_table=True
        
        return [self.x,self.y,self.f]
    
    def move(self,table_obj):
        """
        Moves the robot one unit forward in the current orientation.
        
        Parameters
        ----------
        table_obj: Table.Object
            Tabletop object of class Table.

        Output
        ------
        Returns the pose in [x,y,f] array form
        """ 
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
        """
        Robot turns left - anticlockwise
        
        Output
        ------
        Returns the pose in [x,y,f] array form
        """
        # Looking at f_arr=["EAST","NORTH","WEST","SOUTH"]
        # to go left we need to increase the index by 1
        # if the index is 3 (SOUTH) then wrap around to 0 (EAST)
        next_ind=self.f_arr.index(self.f)+1
        if next_ind>3:
            next_ind=0
        else:
            next_ind
        self.f=self.f_arr[next_ind]
        #Take the value of the next index
        return [self.x,self.y,self.f]
            
    def right(self):
        """
        Robot turns right - clockwise
        
        Output
        ------
        Returns the pose in [x,y,f] array form
        """
        # Looking at f_arr=["EAST","NORTH","WEST","SOUTH"]
        # to go right we need to decrease the index by 1 
        # if the index is 0 (EAST) then wrap around to 3 (SOUTH)
        next_ind=self.f_arr.index(self.f)-1
        if next_ind<0:
            next_ind=3
        else:
            next_ind
        #Take the value of the next index
        self.f=self.f_arr[next_ind]

        return [self.x,self.y,self.f]
        
    def report(self):
        """
        Reports the current pose as an array.
        
        Output
        ------
        Returns the pose in [x,y,f] array form
        """          
        return [self.x,self.y,self.f]
    
    def is_on_table(self):
        """
        Returns if the robot is on the table.
        
        Output
        ------
        Returns the pose in [x,y,f] array form
        """ 
        return self.on_table
    
    def reset(self):
        """
        Resets robot to being off table with no coordinates.
        
        Output
        ------
        Returns the pose in [x,y,f] array form
        """        
        self.x,self.y,self.f=None,None,None
        self.on_table=False
        return [self.x,self.y,self.f]
    
