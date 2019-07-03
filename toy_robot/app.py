"""
Defines the App Class with run method to execute the instruction on the robot given a file
path
Author: William Jiang
"""
import os
import sys
from toy_robot.lib.tr_lib import Table, Robot

class App:
    """
    Class to run the app
    """    
    def run(file_path):
        """
        Method used to run the app via a text file path.

        Attributes:
        -----------
        file_path: string
            Path to text file containing the instructions for the robot. 
        """
        f = open(file_path)
        line = f.readline() 
        robot=Robot() 
        table_top=Table(5,5)
        #loop through every line until end of file
        while line:
            robot.cmd(line,table_top)
            line = f.readline()
        f.close()
        return robot.report()


