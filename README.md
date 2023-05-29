# ENPM661 Planning for Autonomous Robots | Project - 2
```
Name - Krishna Rajesh Hundekari

UID	- 119239049

```
# 1 Dijkstra Algorithm

Implementation of the Dijkstra Algorithm for a Point Robot

Find all the possible 8 connected neighbors and subsequent nodes of those neighbors along with backtracking and visualization

## Video

https://github.com/KrishnaH96/dijkstra_path-planning-algorithm_krishnah/assets/113392023/6c22f92d-eac2-4aed-a769-fd917e4dac75

## Running the code
There are four ways of running a python script which are as follows:

 - You may run it in your operating system's terminal. For e.g., In windows - cmd.
 - Python interactive mode.
 - Integrated Development Environment (IDE) like VSC.
 - Opening the script file from folder

First check the version of python installed in your system by running following command:

*python --version*

If it yields result like this one:

*Python 3.8.10*

## Dependencies

import following modules/library for the script to run correctly: 

*import  numpy as np*  			

*import matplotlib.pyplot as plt*  								

*from queue import PriorityQueue*  			

*import matplotlib.patches as patch*

*import copy*

*import math*								

*import time*  								

## User input

1. Program will prompt to ask the inputs and will ask the X and Y coordinates for start(Home) position and goal position repsectively.
  Please put whole number integer values as input, the program will ask the input until the positions are clear(not in obstacle space).
  Give on coordiate at a time, and put enter to put next coordinate, the code will take all four values in int individually.

2. The program will take sometime to explore far aways points, but quite faster while exploring nearby nodes.
Please be patient while visualising the exploration of the nodes and backtracking the shortest path.



