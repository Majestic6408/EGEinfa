from turtle import *

m = 18
tracer(0)
lt(90)

for i in range(2):
    fd(6 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()

fd(1 * m)
rt(90)
fd(3 * m)
lt(90)

down()

for i in range(2):
    fd(77 * m)
    rt(90)
    fd(45 * m)
    rt(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, 'red')

done()