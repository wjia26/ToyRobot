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
        
