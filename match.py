import math
import random
import visual

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.neighbors = []
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.color) + ")"
    
    def __repr__(self):
        return self.__str__()

class Rectangle:
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
    
    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]x[" + str(self.bottom) + "," + str(self.top) + "]"
    
    def __repr__(self):
        return self.__str__()

def create_random_points(n):
    color = [-1,1]
    random.seed()
    A = list(map(lambda i: [i, random.random(), color[random.randint(0,1)]], range(n)))
    A.sort(key=lambda t: t[1])
    return list(map(lambda t,j: Point(t[0], j, t[2]), A, range(n)))




            
    
