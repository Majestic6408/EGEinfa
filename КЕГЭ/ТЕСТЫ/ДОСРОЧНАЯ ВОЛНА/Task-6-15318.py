from turtle import *

m = 20
tracer(0)
lt(90)

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(18 * m)
    rt(90)

up()

fd(5 * m)
rt(90)
fd(9 * m)
lt(90)

down()
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, 'red')

done()