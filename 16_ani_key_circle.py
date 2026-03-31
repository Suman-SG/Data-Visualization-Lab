import turtle

screen = turtle.Screen()
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()

try:
    direction = input("Enter direction: ").lower()
    speed = int(input("Enter speed: "))
except ValueError:
    print("Invalid speed! Using default speed = 5")
    speed = 5

while True:
    if direction == "up":
        ball.sety(ball.ycor() + speed)
    elif direction == "down":
        ball.sety(ball.ycor() - speed)
    elif direction == "left":
        ball.setx(ball.xcor() - speed)
    elif direction == "right":
        ball.setx(ball.xcor() + speed)