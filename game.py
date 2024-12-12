from math import sin
from math import cos
from math import radians
from turtle import Screen, width, right
import pygame

class Curve:
    def __init__(self,size,n):
        if not size:
            raise ValueError("Missing size.")
        self.size = size
        if not n:
            raise ValueError("Missing n")
        self.n = n 
    
def main():
    curve = get_curve()
    points = []
    for i in range(1,360):
        r = curve.size * sin(radians(curve.n * i))
        x = r * cos(radians(i))
        y = r * sin(radians(i))
        list.append(points, (width/2 + x, right/2 +y))
    pygame.draw.linws(Screen, (0,0,0), False, points, 5)


def get_curve():
    size = int(input("Radius of curve: "))
    n = int(input("Number of petals: "))
    return Curve(size, n)