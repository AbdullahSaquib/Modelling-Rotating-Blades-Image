import turtle
from rfb import Blade
from conversions import deg_to_rad
import math as m


w = deg_to_rad(10)
omg = deg_to_rad(5)
Blade.set_ts(1)


# Create four Blades of width w, and different initial positions
b1 = Blade(0, w, omg)
b2 = Blade(m.pi/2, w, omg)
b3 = Blade(m.pi, w, omg)
b4 = Blade(3*m.pi/2, w, omg)


#  Following code is used to draw images


r = 100  # radius of the fan blades
p = 0  # initial angular position of the turtle
dp = 1  # angular position to be incremented by 1 degree

turtle.speed(0)
turtle.pensize(2)
turtle.colormode(255)
turtle.tracer(0)
turtle.setup(height=250, width=250)


""" The following while loop loops over various angular positions,
    evaluate redefined opacities at at these postions, and draw a
    line from "origin" to the end of blade.
"""

while p < 360:
    p_rad = deg_to_rad(p)
    col = int((1 - (b1.Pr(p_rad) + b2.Pr(p_rad) +
                    b3.Pr(p_rad) + b4.Pr(p_rad)))*255)
    turtle.setposition(0, 0)
    turtle.color(col, col, col)
    turtle.forward(r)
    turtle.left(dp)
    p += dp

    
""" But a black dot at the center of the image, to give an idea of 
    center of the fan.
"""
turtle.setposition(0, 0)
turtle.dot(20, 'black')


# Store image as .eps file
ts = turtle.getscreen()
ts.getcanvas().postscript(file='omg5ts1.eps')

print(turtle.position())
turtle.done()
