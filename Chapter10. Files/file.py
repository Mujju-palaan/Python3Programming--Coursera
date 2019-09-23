fileref = open("olympics.txt","r")
line = fileref.readlines()

for i in line[:4]:
    print(i)
fileref.close()