from turtle import *

## Task 1: Look at the following code and decide which picture it will generate.
# Then download it from the shared drive, then save and run it, to check.

def demo():
  pencolor("blue")
  speed(120)
  for counter in range (100):
    right(66)
    fd(150)
    


#3.	The following code will draw a petal of a
#flower. Use the code in a for loop to make a
#flower as shown on the right.

def petal():
    for counter in range(6):
        circle(50,120)
        left(60)
        circle(50,120)

def flower():
    for flowey in range(6):
        petal()
        right(3)
    
flower()