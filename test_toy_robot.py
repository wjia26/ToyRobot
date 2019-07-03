"""
Toy Robot Unit/Integration Testing
Author: William Jiang
"""
import os
import sys
import unittest
from toy_robot.lib.tr_lib import Table, Robot
from toy_robot.app import App
directory='toy_robot/test_cases/'

class RobotTest(unittest.TestCase):
    def setUp(self):
        """
        Setup and initilialize pose for robot/table.
        """
        self.robot=Robot()
        self.table_top=Table(5,5)
        self.robot.place(1,1,'WEST',self.table_top)

    def tearDown(self):
        """
        Teardown after completion of unit test.
        """        
        self.robot.reset()
        
    def test_table(self):
        """
        Unit test for Table.get_dim method
        """
        self.assertEqual(self.table_top.get_dim(),(5,5))
        
    def test_reset(self):
        """
        Unit test for Robot.reset method
        """
        self.assertEqual(self.robot.reset(),[None,None,None])
        
    def test_cmd(self):
        """
        Unit test for Robot.cmd method
        """
        self.assertEqual(self.robot.cmd('REPORT',self.table_top),[1,1,'WEST'])
        
    def test_place(self):
        """
        Unit test for Robot.place method
        """
        self.assertEqual(self.robot.reset(),[None,None,None])
        self.assertEqual(self.robot.place(1,1,'WEST',self.table_top),[1,1,'WEST'])
        
    def test_move(self):
        """
        Unit test for Robot.move method
        """
        self.robot.place(1,1,'WEST',self.table_top)
        self.assertEqual(self.robot.move(self.table_top),[0,1,'WEST'])
        
    def test_left(self):
        """
        Unit test for Robot.left method
        """
        self.assertEqual(self.robot.left(),[1,1,'SOUTH'])
        
    def test_right(self):
        """
        Unit test for Robot.right method
        """
        self.assertEqual(self.robot.right(),[1,1,'NORTH'])
        
    def test_report(self):
        """
        Unit test for Robot.report method
        """
        self.assertEqual(self.robot.report(),[1,1,'WEST'])
        
    def test_is_on_table(self):
        """
        Unit test for Robot.is_on_table method
        """
        self.assertEqual(self.robot.is_on_table(),True)       
    
    def test_full(self):
        """
        Full Integration test. Loops through the 5 test cases in ./test_cases and compares to solutions.
        """
        solutions=[
            [0,5,"NORTH"],
            [0,0,"WEST"],
            [3,3,"NORTH"],
            [2,5,"WEST"],
            [None,None,None]
            ]
        n=0
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                report=App.run(directory + filename)
            self.assertEqual(report,solutions[n])
            n=n+1

        
            
if __name__ == "__main__":
    """
    Runs Unit tests from the test_cases folder and loops through each line of instruction.
    Instructions are then fed into an instiantiated Robot Object called: "robot"
    Two classes are used from the lib directory: Table, Robot. 
    """
    unittest.main()
    
