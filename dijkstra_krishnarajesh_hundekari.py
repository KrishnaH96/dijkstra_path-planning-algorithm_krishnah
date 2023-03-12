import math
from queue import PriorityQueue
import matplotlib.pyplot as plt
import numpy as np
import copy


def line_equation(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
       
    y_intercept = y1 - slope * x1
    
    return slope, y_intercept

def boundry_limit(x,y):

    if x >= 5 and x <= 595 and y >= 5 and y <= 245:
        return False
    
    else:
        return True

def bottom_rect(x,y):

    if x >= 95 and x <= 155 and y <= 105 and y >= 0:
        return True
    else:
        return False
    
def upper_rect(x,y):

    if x >= 95 and x <= 155 and y>= 145 and y <= 250:
        return True
    else:
        return False   
    

def hexagon_obt(x,y):

    # h_l1 = line_equation(235.05 - 5, 162.5 + 5,300, 200 + 5)
    h_l1 = line_equation(230.05, 165.38,300, 205.77)
    l1= y - h_l1[0] * x - h_l1[1]

    # h_l2 = line_equation(300, 200 + 5, 364.95 + 5, 162.5 + 5)
    h_l2 = line_equation(300, 205.77, 369.95, 165.38)
    l2 = y - h_l2[0] * x - h_l2[1]

    # h_l3 = line_equation(364.95 + 5, 87.5 - 5, 300, 50 -5)
    h_l3 = line_equation(369.95, 84.61, 300, 44.22)
    l3 = y - h_l3[0] * x - h_l3[1]

    # h_l4 = line_equation(300, 50 -5, 235.05 - 5, 87.5 - 5)
    h_l4 = line_equation(300, 44.22, 230.04, 84.61)
    l4 = y - h_l4[0] * x - h_l4[1]
    

    if x >= (230.04) and x <= (369.95) and l1 <= 0 and l2 <= 0 and l3 >= 0 and l4 >= 0:
        return True
    
    else:
        return False

def triangle_obt(x,y):

    # t_l1 = line_equation(460 -5, 225+5, 515,125)
    t_l1 = line_equation(455, 246.18, 515.59,125)
    l5= y - t_l1[0] * x - t_l1[1]

    # t_l2 = line_equation(515,125, 460 -5, 25-5)
    t_l2 = line_equation(515.59,125,455, 3.81)
    l6 = y - t_l2[0] * x - t_l2[1]

    if x >= (455) and l5 <= 0 and l6 >= 0:
        return True
    else:
        return False
    
    
def obstacle_check(node_pose):

    x = node_pose[0]
    y= node_pose[1]

    if bottom_rect(x,y) or upper_rect(x,y) or hexagon_obt(x,y) or triangle_obt(x,y) or boundry_limit(x,y):
        return True
    else:
        return False
    

home_x = int(input("Hey!! Where to start? Please enter home 'x' coordinate:  \n"))
home_y = int(input("Please enter home 'y' coordinate: \n"))
home_loc = (home_x, home_y)
while obstacle_check(home_loc):
    print("The entered value is in the obstacle. Please enter new values\n")
    home_x = int(input("Hey!! Where to start? Please enter home 'x' coordinate:  \n"))
    home_y = int(input("Please enter home 'y' coordinate: \n"))
    home_loc = (home_x, home_y)


goal_x = int(input("Now give the goal 'x' coordinate \n")) 
goal_y = int(input("Please enter goal 'y' coordinate \n"))
goal_loc = (goal_x, goal_y)
while obstacle_check(goal_loc):
    goal_x = int(input("Now give the goal 'x' coordinate \n")) 
    goal_y = int(input("Please enter goal 'y' coordinate \n"))
    goal_loc = (goal_x, goal_y)


x_visited = [] 
y_visited = [] 
start_pose = home_loc
goal_pose = goal_loc

# start_pose = (10, 10)
# goal_pose = (180, 98)

c2c = 0
parent_pose = None
adam_node = (c2c,(parent_pose),(start_pose))
open_list = PriorityQueue()
open_list.put(adam_node)

closed_list = {} 

def left_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]-1
    updated_y = node_in_action[2][1]
    current_child = (updated_x, updated_y)

    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))

def right_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]+1
    updated_y = node_in_action[2][1]
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))
            

def up_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]
    updated_y = node_in_action[2][1]+1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))

def down_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]
    updated_y = node_in_action[2][1]-1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))


def up_left_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1.4
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]-1
    updated_y = node_in_action[2][1]+1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))

def up_right_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1.4
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]+1
    updated_y = node_in_action[2][1]+1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))


def down_left_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1.4
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]-1
    updated_y = node_in_action[2][1]-1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))

def down_right_move(node):
    node_in_action = copy.deepcopy(node)
    c2c_moved = node_in_action[0]+1.4
    current_parent = node_in_action[2]
    updated_x = node_in_action[2][0]+1
    updated_y = node_in_action[2][1]-1
    current_child = (updated_x, updated_y)
    
    if obstacle_check(current_child) == False:
        if current_child not in closed_list:
            for i in range(0,(open_list.qsize())):
                if open_list.queue[i][2] == current_child and open_list.queue[i][0] > c2c_moved:
                    open_list.queue[i][1] == current_parent
            open_list.put((c2c_moved, current_parent, current_child))


while True:


    current_node = open_list.get() 

    if current_node[2] in closed_list: 
        continue


    x_visited.append(current_node[2][0]) 
    y_visited.append(current_node[2][1])


    closed_list[current_node[2]] = (current_node[1]) 
    if current_node[2] == goal_pose: 
        print("Mission Accomplished...Goal Reached")
        print(current_node)
        break
        
    else:

        left_move(current_node)
        right_move(current_node)
        up_move(current_node)
        down_move(current_node)

        up_left_move(current_node)
        down_left_move(current_node)
        up_right_move(current_node)
        down_right_move(current_node)
     



