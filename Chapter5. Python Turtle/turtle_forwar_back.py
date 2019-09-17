import turtle
wn = turtle.Screen()
mujju = turtle.Turtle()
mujju.shape("turtle")
mujju.speed(100)

d = 100
a = 0
mujju.up()


for i in range(12):
    
    mujju.forward(d) 
    mujju.stamp()
    mujju.backward(d)
    mujju.right(a + 30 )
    
    

    


