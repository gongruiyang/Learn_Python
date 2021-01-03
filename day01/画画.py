import turtle as t
from random import randint as rint
t.shape("turtle")
t.pensize(1)
t.colormode(255)
t.bgcolor("black")
t.tracer(False)
for x in range(350):
    t.forward(2 * x)
    t.color(rint(0,255),rint(0,255),rint(0,255))
    t.left(90)
    t.speed(10)
    t.tracer(True)
t.done()
