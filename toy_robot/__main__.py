"""
Toy Robot Simulation
Takes text file as input and outputs the pose.
Author: William Jiang
"""
import os
import sys
import argparse
from toy_robot.app import App

          
if __name__ == "__main__":
    """
    Reads Path to text file from stdin and loops through each line of instruction.
    Instructions are then fed into an instiantiated Robot Object called: "robot"
    Two classes are used from the lib directory: Table, Robot. 
    """
    #Add argument to parse from command line. Will locate the text file required for the instructions
    ap = argparse.ArgumentParser(description='Toy Robot Application')
    ap.add_argument('-t','--textfile', help="Path to text file containing Robot instructions")
    args=vars(ap.parse_args())
    #Run application from app.py with the file path as input
    report_arr=App.run(args["textfile"])
    print(str(report_arr[0]) + ',' + str(report_arr[1])+ ',' + report_arr[2])
    

