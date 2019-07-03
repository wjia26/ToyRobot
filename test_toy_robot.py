"""
Toy Robot Unit/Integration Testing
Author: William Jiang
"""
import os
import sys
import unittest
from toy_robot.lib.tr_lib import Table
directory='toy_robot/test_cases/'

class RobotTest(unittest.TestCase):
        
    def test_table(self):
        """
        Unit test for Table.get_dim method
        """
        self.assertEqual(self.table_top.get_dim(),(5,5))
        
            
if __name__ == "__main__":
    """
    Runs Unit tests from the test_cases folder and loops through each line of instruction.
    Instructions are then fed into an instiantiated Robot Object called: "robot"
    Two classes are used from the lib directory: Table, Robot. 
    """
    unittest.main()
    
