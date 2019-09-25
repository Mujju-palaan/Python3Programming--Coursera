def square(x):
	    y = x * x
	    return y
	
def sum_of_squares(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
	
    return a+b+c
	
a = -5
b = 2
c = 10
result = sum_of_squares(a,b,c)
print(result)