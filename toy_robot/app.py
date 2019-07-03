import os
import sys
from toy_robot.lib.tr_lib import Table, Robot
class App:
    def run(file_path):
        f = open(file_path)
        line = f.readline() 
        robot=Robot() 
        table_top=Table(5,5)
        while line:
            robot.cmd(line,table_top)
            line = f.readline()
        f.close()


