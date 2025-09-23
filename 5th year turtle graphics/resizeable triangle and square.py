from turtle import *

def square(square_sides_length):
    for counter in range(4):
        forward(square_sides_length)
        right(90)

def triangle(triangle_sides_length):
    for tringle in range(3):
        fd(triangle_sides_length)
        left(120)
square_sides_length = int(input("what size doe you want your square to be? "))
triangle_sides_length = int(input("what size doe you want your triangle to be? "))
square(square_sides_length)
triangle(triangle_sides_length)
