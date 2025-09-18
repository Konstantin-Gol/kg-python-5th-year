from turtle import *

def triangle():
    fillcolor("cyan")
    begin_fill()
    pencolor("black")
    for counter in range(3):
        fd(100)
        left(120)
    end_fill()
    
triangle()
        