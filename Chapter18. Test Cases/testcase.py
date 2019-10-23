class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

import test

#testing instance variables x and y
p = Point(3, 4)
test.testEqual(p.y, 4)
test.testEqual(p.x, 3)

#testing the distance method
p = Point(3, 4)
test.testEqual(p.distanceFromOrigin(), 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
test.testEqual(p.x, 1)
test.testEqual(p.y, 7)
