import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()    # create alex
drawSquare(alex, 50)      # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()
