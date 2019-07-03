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
    #Add argument to parse from command line. Will locate the text file required for the instructions
    ap = argparse.ArgumentParser(description='Toy Robot Application')
    ap.add_argument('-t','--textfile', help="Path to text file containing Robot instructions")
    args=vars(ap.parse_args())
    #Run application from app.py with the file path as input
    report_arr=App.run(args["textfile"])
    print(str(report_arr[0]) + ',' + str(report_arr[1])+ ',' + report_arr[2])
    

