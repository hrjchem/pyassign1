import turtle
import math
colors=['blue','green','red','black','orange','purple']
for i in range(6):
    t[i]=turtle.Turtle()

def orbit():
    for i in range(6):
        t[i].up()
        t[i].goto(0,40*i+40)
        t[i].down()
    for j in range(360):
        while True:
            x=j*2*math.pi/360
            for i in range(6):
                t[i].shape('circle')
                t[i].color(colors[i])
                t[i].goto((40*i+40)*math.sin(x*(i+1)),(40*i+40)*math.cos(x*(i+1))
orbit()
