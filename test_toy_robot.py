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
    def setUp(self):
        self.robot=Robot()
        self.table_top=Table(5,5)

    def tearDown(self):
        
    def test_table(self):
        """
        Unit test for Table.get_dim method
        """
        self.assertEqual(self.table_top.get_dim(),(5,5))

    def test_place(self):
        self.assertEqual(self.robot.place(1,1,'WEST',self.table_top),[1,1,'WEST'])
        
            
if __name__ == "__main__":
    unittest.main()
    
