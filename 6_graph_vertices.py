import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("cyan")
pen.speed(0)
pen.penup()

# User input
n = int(input("Enter number of vertices: "))

# Store vertex positions
vertices = []

radius = 150

# Create vertices in circular layout
for i in range(n):
    angle = 2 * math.pi * i / n
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Draw vertices
for (x, y) in vertices:
    pen.goto(x, y)
    pen.dot(10, "yellow")

# Draw edges (complete graph)
pen.color("white")

for i in range(n):
    for j in range(i + 1, n):
        pen.penup()
        pen.goto(vertices[i])
        pen.pendown()
        pen.goto(vertices[j])

turtle.done()