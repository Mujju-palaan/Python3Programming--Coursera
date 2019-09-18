#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.



words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for word in words:
    if word[-1] == 'e':
        
        past_tense.append(word + "d")
    else :
        
        past_tense.append(word + "ed")
        
print(past_tense)
     
##################################
# Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

# HINT 1: Use the accumulation pattern!

# HINT 2: the in operator checks whether a substring is present in a string.

# Hard-coded answers will receive no credit.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    
    if "w" in i[0:]:
        
        acc_num += 1
                   
print(acc_num)   
    

#####################################
# Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

# Note 1: be sure to not double-count words that contain both an a and an e.

# HINT 1: Use the in operator.

# HINT 2: You can either use or or elif.

# Hard-coded answers will receive no credit.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
words = sentence.split()
num_a_or_e = 0
for word in words:
    
    if "a" in word[0:]:
        print("mujju")
        num_a_or_e += 1
    elif "e" in word[0:]:
        print("mujju")
        num_a_or_e += 1
        
        
print(num_a_or_e)
        

##########################
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = []
words = s.split()
print(words)
num_vowels = 0

for vowels in words:
    print(words.count(vowels))
    num_vowels += 1
    
print(num_vowels)
    
    
   





   
        
        
            
        
    

