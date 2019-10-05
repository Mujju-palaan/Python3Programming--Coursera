def sublist(x):
    sub = []
    x = (num for num in x) 
    num = next(x, 5)  
    while num != 5:
        sub.append(num)
        num = next(x, 5)  
    return sub

x = [1, 3, 4, 5, 6, 7, 3]
print(sublist(x))


#####################################

def check_nums(x):
    sub = []
    x = (num for num in x) 
    num = next(x, 7)  
    while num != 7:
        sub.append(num)
        num = next(x, 7)  
    return sub

x = [1, 3, 4, 5, 6, 7, 3]
print(check_nums(x))

#######################################
def sublist(list):
   i = 0
   while i < len(list):

       if (list[i] == 'STOP'):
           return list[0:i]
       i+=1
   return list[0:i]
print(sublist(['mujju','salman','yo','STOP']))
