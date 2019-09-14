import turtle
wn = turtle.Screen()
wn.bgcolour("ligthgreen")
mujju = turtle.Turtle()
mujju.color("red")
mujju.shape("turtle")

d = 5
mujju.up()
for i in range(30):
    mujju.stamp()
    mujju.forward(d)
    mujju.right(24)
    d = d + 2

wn.exitonclick()

