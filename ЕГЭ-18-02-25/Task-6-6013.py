from turtle import *

m = 6
tracer(0)
lt(90)

for i in range(2):
    rt(120)
    fd(7 * m)

rt(300)

for i in range(2):
    rt(120)
    fd(7 * m)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'red')

done()