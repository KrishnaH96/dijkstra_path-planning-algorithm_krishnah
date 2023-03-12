import math
from queue import PriorityQueue
import matplotlib.pyplot as plt
import numpy as np

def line_equation(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    
    
    y_intercept = y1 - slope * x1
    
    return slope, y_intercept


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

    h_l1 = line_equation(235.05 - 5, 162.5 + 5,300, 200 + 5)
    l1= y - h_l1[0] * x - h_l1[1]

    h_l2 = line_equation(300, 200 + 5, 364.95 + 5, 162.5 + 5)
    l2 = y - h_l2[0] * x - h_l2[1]

    h_l3 = line_equation(364.95 + 5, 87.5 - 5, 300, 50 -5)
    l3 = y - h_l3[0] * x - h_l3[1]

    h_l4 = line_equation(300, 50 -5, 235.05 - 5, 87.5 - 5)
    l4 = y - h_l4[0] * x - h_l4[1]

    if x >= (235.05-5) and x <= (364.95+5) and l1 <= 0 and l2 <= 0 and l3 >= 0 and l4 >= 0:
        return True
    else:
        return False

def triangle_obt(x,y):

    t_l1 = line_equation(460 -5, 225+5, 515,125)
    l5= y - t_l1[0] * x - t_l1[1]

    t_l2 = line_equation(515,125, 460 -5, 25-5)
    l6 = y - t_l2[0] * x - t_l2[1]

    if x >= (460-5) and l5 <= 0 and l6 >= 0:
        return True
    else:
        return False
    
def obstacle_check(x,y):

    if bottom_rect(x,y) or upper_rect(x,y) or hexagon_obt(x,y) or triangle_obt(x,y):
        return True
    else:
        return False
    




