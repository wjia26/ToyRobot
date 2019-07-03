README
===================

Introduction
-----------
This package simulates the Toy Robot as per PROBLEM.md

Usage
-----------
Change directory to ../ToyRobot/
Write your instruction inputs in a .txt file and paste it in a location within the repo.

The package can be run via the command-line:

    python -m toy_robot -t path/to/testfile

    i.e. python -m toy_robot -t testexample.txt
    
Unit/Integration testing
-----------
The unit testing can be run via the command-line:

    python test_toy_robot.py

Examples
------------------------

### Example a
Example input text file:

    PLACE 0,0,NORTH
    MOVE
    REPORT

Expected output:

    0,1,NORTH

