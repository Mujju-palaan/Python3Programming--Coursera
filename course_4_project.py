VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self, initName):
        self.name = initName
        self.prizeMoney = 0
        self.prizes = []
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    def __str__(self):
        state = self.name + " ($" + str(self.prizeMoney) + ")"
        return state
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(category, obscuredPhrase, guessed):
        str = input(self.name + "has $"+ str(self.prizeMoney)+ "/n" + ", Category:" + category + "/n" + ", Phrases:" + "/n" + obscuredPhrase + "/n" + ", Guessed:" + guessed + "/n" + "Guess a letter, phrase, or type 'exit' or 'pass':") 
        print(str)
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    prizemoney = 0
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        if random.randint(1, 10) > self.difficulty:
            return True
        else: 
            return False
    
    def getPossibleLetters(self, guessed):
        list = []
        if self.prizemoney >= 250: 
            for l in LETTERS:
                list.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    list.append(l)
        return list

    def getMove(self, category, obscuredPhrase, guessed):
        list = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(list) == 0:
            return 'pass'
        else:
            if FlipResult==True:
                for l in self.SORTED_FREQUENCIES:
                    if l in list:
                        return l
            elif FlipResult==False:
                return random.choice(list)
