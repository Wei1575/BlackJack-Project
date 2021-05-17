class Card: 
    def __init__(self, SVAL, value, suit = "", name = ""): 
        self.value = value
        if(SVAL == 1):
            self.suit = "clubs"
        if(SVAL == 2):
            self.suit = "diamonds"
        if(SVAL == 3):
            self.suit = "hearts"
        if(SVAL == 4):
             self.suit = "spades"
        if(value == 1):
            self.name = "ace of " + self.suit
        if(value>1 and value<11):
            self.name = str(value) + " of " + self.suit
        if(value == 11):
            self.name = "jack of " + self.suit
        if(value == 12):
            self.name = "queen of " + self.suit
        if(value == 13):
            self.name = "king of " + self.suit  
          
