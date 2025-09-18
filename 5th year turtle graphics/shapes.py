from turtle import *

def square():
    fillcolor("green")
    begin_fill()
    pencolor("black")
    fd(100)
    right(90)
    fd(100)
    right(90)
    fd(100)
    right(90)
    fd(100)
    end_fill()
    

def triangle():
    fillcolor("purple")
    begin_fill()
    pencolor("black")
    fd(100)
    left(120)
    fd(100)
    left(120)
    fd(100)
    left(120)
    end_fill()

square()
penup()
fd(100)
pendown()
triangle()

penup()
left(90)
forward(200)
pendown()
circle(80)
penup()
left(90)
forward(40)
right(90)
pendown()
circle(40)



    
