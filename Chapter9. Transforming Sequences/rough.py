b = ['q', 'u', 'i']
z = b
b[1] = 'i'
print(b)
z.remove('i')
print(z)
#############################
v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))
###################
alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)
#################
list= [3,0,9,4,1,7]
new_list=[]
for i in range(len(list)):
   new_list.append(list[i]+5)
print(new_list)