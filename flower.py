import turtle
from turtle import*


t = turtle.Turtle()
for i in range(8): #limits repeat of circles to 8
    t.speed(50) #modify speed of turtle
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(50)
    t.left(45)
    t.end_fill()
