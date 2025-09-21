from turtle import *

def hexagon():
    fillcolor("blue")
    begin_fill()
    pencolor("black")
    for counter in range(6):
        for sector in range(3):
            fd(50)
            left(120)
        left(60)
    end_fill()

def pentagon():
    for hexagon in range(5):
        left(72)
        fd(200)

pen_up()
fd(50)
pen_down()
pentagon()

hexagon()

