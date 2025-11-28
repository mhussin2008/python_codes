import math as m
import turtle

t=turtle.Turtle()
t.speed(0)
print(m.pi)
length=1
multiplier=50
watar=m.sqrt(2)
t.forward(multiplier)


t.left(90)
t.forward(multiplier*length)
current_position = t.pos()
watar=m.sqrt(2)
theta=m.atan(1)*180/m.pi
print(theta)

for i in range(100):
    t.left(180-theta)
    t.forward(watar*multiplier)
    t.goto(current_position)
    t.right(90)
    t.forward(multiplier)
    current_position = t.pos()
    theta=m.atan(watar)*180/m.pi
    watar=m.sqrt(watar**2+1)
   


#t.right(90)
#t.forward(100)
#t.left(125)
#t.forward(175)


turtle.Screen().exitonclick()
#turtle.done()
