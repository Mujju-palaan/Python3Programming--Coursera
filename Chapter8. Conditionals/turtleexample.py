import turtle
wn = turtle.Screen()
mujju = turtle.Turtle()

mujju.pencolor("blue")
mujju.forward(50)
if mujju.pencolor() == "blue":
    mujju.right(60)
    mujju.forward(100)
else:
    mujju.left(60)
    mujju.forward(100)

thuss = turtle.Turtle()
thuss.forward(60)
if thuss.pencolor() == "blue":
    thuss.right(60)
    thuss.forward(100)
else:
    thuss.left(60)
    thuss.forward(100) 

########################################################

import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.right(170)

colors = ["Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Orange", "Pink", "Pink", "Orange", "Yellow", "Purple", "Orange", "Purple", "Yellow", "Orange", "Pink", "Orange", "Purple", "Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Yellow"]


for color in colors:
    if amy.pencolor() == "Purple":
        amy.forward(50)
        amy.right(59)
    elif amy.pencolor() == "Yellow":
        amy.forward(65)
        amy.left(98)
    elif amy.pencolor() == "Orange":
        amy.forward(30)
        amy.left(60)
    elif amy.pencolor() == "Pink":
        amy.forward(50)
        amy.right(57)

    amy.pencolor(color)
