# week 4 Loops

from turtle import *#imports the entire library
#(import turtle) command only imports turtle. #needs t.forward to pull from library

def eldrich_horror_cube():
    speed(1000)#speeeeed baby
    for counter in range(100):#python starts from 0 and stops the code when the counter reaches 100
        forward(100)
        right(90)
        left(1)

eldrich_horror_cube()