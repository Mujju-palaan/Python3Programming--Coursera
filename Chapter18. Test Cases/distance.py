import test
def distance(x1, y1, x2, y2):
    return 0.0

test.testEqual(distance(1, 2, 1, 2), 0)


import test
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

test.testEqual(distance(1,2, 1,2), 0)
test.testEqual(distance(1,2, 4,6), 5)
