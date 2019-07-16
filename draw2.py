import turtle
from rfb import Blade
from conversions import deg_to_rad
import math as m


r = 100
dp = 1


for i in range(360, 361, 10):
    p = 0
    w = deg_to_rad(10)
    if i == 0:
        omg = deg_to_rad(0.001)
    else:
        omg = deg_to_rad(i)
    print(i)
    Blade.set_ts(1)
    b1 = Blade(0, w, omg)
    b2 = Blade(m.pi/2, w, omg)
    b3 = Blade(m.pi, w, omg)
    b4 = Blade(3*m.pi/2, w, omg)

    turtle.speed(0)
    turtle.pensize(2)
    turtle.colormode(255)
    turtle.tracer(0)
    turtle.setup(height=250, width=250)
    while p < 360:
        p_rad = deg_to_rad(p)
        col = int((1 - (b1.Pr(p_rad) + b2.Pr(p_rad) +
                        b3.Pr(p_rad) + b4.Pr(p_rad)))*255)
        turtle.setposition(0, 0)
        turtle.color(col, col, col)
        turtle.forward(r)
        turtle.left(dp)
        p += dp

    turtle.setposition(0, 0)
    turtle.dot(20, 'black')

    ts = turtle.getscreen()
    ts.getcanvas().postscript(file='omg'+str(i)+'.eps')
    turtle.clearscreen()

print(turtle.position())
turtle.done()
