from turtle import *

def envelope():
    for square in range (4):
        right(90)
        fd(100)
    right(150)
    for triangle in range (2):
        fd(50)
        left(180)

envelope()