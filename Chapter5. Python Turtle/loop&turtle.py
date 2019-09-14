import turtle

turtle.Screen()
mujju = turtle.Turtle()

distance = 50
for i in range(20):
    mujju.forward(distance)
    mujju.right(90)
    distance = distance + 10