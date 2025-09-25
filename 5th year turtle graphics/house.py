from turtle import *

def square(length):
    color(colour1)
    for counter in range(4):
        forward(length)
        right(90)

def triangle(length):
    color(colour2)
    for tringle in range(3):
        fd(length)
        left(120)
        
def door(length):
    penup()
    fd(length/3)
    right(90)
    fd(length)
    left(90)
    pendown()
    for doour in range(4):
        fd(length/3)
        left(90)
    
def house(length):
    triangle(length)
    square(length)
    door(length)

length = int(input("what size is the house? "))
colour1 = input("what colour is the house? ")
colour2 = input("what colour is the roof? ")
house(length)
        

        
