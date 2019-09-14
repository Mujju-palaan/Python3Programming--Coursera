import turtle
wn = turtle.Screen()
triangle = turtle.Turtle()
square = turtle.Turtle()
hexagon = turtle.Turtle()
octagon = turtle.Turtle()
d = 50

for i in range(3):
    triangle.forward(d)
    triangle.left(120)
for i in range(4):
    square.forward(d)
    square.left(90)
for i in range(6):
    hexagon.forward(d)
    hexagon.left(60)
for i in range(8):
    octagon.forward(d)
    octagon.left(45)
wn.exitonclick()