#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app = []
for i in ael:
    app.append(i)

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for i in wrds:
    i = i + "ed"
    past_wrds.append(i)
    

#