from turtle import *
# screensize(1920,1080)
# tracer(0)
# m = 11
#
# for i in range(2):
#     fd(5 * m)
#     rt(90)
#     fd(11 * m)
#     rt(90)
#
# up()
#
# fd(-4 * m)
# rt(90)
# fd(6 * m)
# lt(90)
#
# down()
#
# for i in range(2):
#     fd(42 * m)
#     rt(90)
#     fd(63 * m)
#     rt(90)
#
# up()
#
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x * m, y * m)
#         dot(4, 'red')
#
# done()

#2
screensize(7000, 7000)
m = 11
tracer(0)

rt(45)
for i in range(10):
    rt(45)
    fd(203 * m)
    rt(45)

up()

bk(40 * m)
rt(45)

down()

for i in range(5):
    fd(20 * m)
    lt(90)

up()

for x in range(-500, 50):
    for y in range(-500, 30):
        goto(x * m, y * m)
        dot(4,'red')

done()

