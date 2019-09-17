week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
temp = week_temps_f.split(",")
# for i in temp:
#     return i + i
#avg_temp = float(sum(temp))/len(temp)
print(temp)

original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_list = original_str.split()
print(original_list)
num_words = len(original_list)
num_words_list = []
for i in original_list:
    num_words_list.append((len(i)))
print(num_words_list)


lett = ""

for i in range(7):
    i = "b"
    lett += i
print(lett)

import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

# move the turtle forward a little so that the whole path fits on the screen
lovelace.penup()
lovelace.forward(60)

# now draw the drunk pirate's path
lovelace.pendown()
current_heading = 0
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:

    # we use .left() so that positive angles are counter-clockwise
    # and negative angles are clockwise
    current_heading = (current_heading + angle) % 360
    lovelace.left(angle)
    lovelace.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", current_heading)

wn.exitonclick()


