import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle (circle)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()

# Initial position
ball.goto(-200, 0)

# Animation loop
while True:
    ball.forward(2)  # move right

    # If it reaches boundary, go back
    if ball.xcor() > 200:
        ball.goto(-200, 0)