#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
yoo = open("travel_plans.txt","r")
line = yoo.read()
num = 0
for char in line:
    
    num = num + 1
print(num)

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
yoo = open("emotion_words.txt","r")
line = yoo.read()
homie = line.split()
num_words = 0
print(homie)
for word in homie:
    num_words = num_words + 1
print(num_words)

#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
yoo = open("school_prompt.txt","r")
line = yoo.readlines()
print(line)
num_lines = 0

for word in line:
    num_lines = num_lines + 1
print(num_lines)

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
yoo = open("school_prompt.txt","r")
line = yoo.readlines()
print(line)
s = 0
beginning_chars =""

for mujju in line[:1]:
    
    beginning_chars = beginning_chars + mujju[:30]
    
    
print(beginning_chars)

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
yoo = open("school_prompt.txt","r")
lines = yoo.readlines()

three = []

for line in lines:
    
    w = line.split()
    print(w)
    three.append(w[2])
print(three)    

#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions = []
yoo = open("emotion_words.txt","r")
lines = yoo.readlines()
for line in lines:
    
    word = line.split()
    print(word[0])
    emotions.append(word[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
first_chars = ''
yoo = open("travel_plans.txt","r")
line = yoo.readline()
print(line[:32])
first_chars = first_chars + line[:33]
print(first_chars)

#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words = []
yoo = open("school_prompt.txt","r")
lines = yoo.readlines()
for line in lines:
    word = line.split()
    for i in word:
        
        if 'p' in i:
            print(i)
            p_words.append(i)
print(p_words)