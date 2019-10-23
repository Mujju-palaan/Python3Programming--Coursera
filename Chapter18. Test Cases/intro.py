def square(x):
    '''raise x to the second power'''
    return x * x

import test
print('testing square function')
test.testEqual(square(10), 100)
