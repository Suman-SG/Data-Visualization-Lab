import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Keyboard Controlled Circle")

# Create circle (player)
player = turtle.Turtle()
player.shape("circle")
player.color("cyan")
player.penup()
player.speed(0)

# Movement functions
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Keyboard binding
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Keep window open
turtle.done()