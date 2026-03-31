import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.penup()

for x in range(-200, 200):
    y = 50 * math.sin(x * 0.05)
    pen.goto(x, y)
    pen.pendown()

turtle.done()