import random 
class BlackJack:

    def __init__(self, hand = [], value = 0):
        self.hand = []
        self.value = 0
    
    def addCard(self, deck):
        temp = random.randint(0,len(deck)-1)
        self.hand.append(deck[temp])
        deck.remove(deck[temp])
    
    def clearAll(self):
        self.hand = []
        self.value = 0

    def getValue(self):
        self.value = 0
        aceCount = 0;
        for card in range(0,len(self.hand)):
            if(self.hand[card].value == 1):
                aceCount += 1
            else:
                self.value += self.hand[card].value
        self.value = self.betterAceVal(self.value, aceCount);
        return self.value
   
    def betterAceVal(self, value, count):
        if(count == 0):
	    return value;
        if(value+10+count <= 21):
            return value+10+count
        else:
            return value+count
