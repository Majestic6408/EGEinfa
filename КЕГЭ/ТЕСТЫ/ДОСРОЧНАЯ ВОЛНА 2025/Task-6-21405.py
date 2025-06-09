from turtle import *

screensize(2000, 2000)
m = 50
tracer(0)
lt(90)

rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4, 'red')

done()