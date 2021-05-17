import random
import time

def printstop(*stuff): #Prints out stuff then sleeps for 2 seconds
  for x in stuff:
    print(x, end = "")
  time.sleep(2)
  print("\n")

def Game(bet):
  player = BlackJack()
  Justin = BlackJack()
  Karina = BlackJack()
  Michelle = BlackJack()
  dealer = BlackJack()
  deck1 = []
  for a in range(1,5):
    for b in range(1,14):
      deck1.append(Card(a,b))

  player.clearAll()
  Justin.clearAll()
  Karina.clearAll()
  Michelle.clearAll()
  dealer.clearAll()

  player.addCard(deck)
  player.addCard(deck)
  player.getValue()
  Justin.addCard(deck)
  Justin.addCard(deck)
  Justin.getValue()
  Karina.addCard(deck)
  Karina.addCard(deck)
  Karina.getValue()
  Michelle.addCard(deck)
  Michelle.addCard(deck)
  Michelle.getValue()
  dealer.addCard(deck)
  dealer.addCard(deck)

  printstop("Everyone gets 2 cards to start")
  printstop("The dealer reveals one of this cards: ", dealer.hand[0].name)
  printstop("Here are you cards: ", player.hand[0].name, " and ", player.hand[1].name)
  printstop("Your hand's value is ", player.getValue())
  
  if(player.value == 21):
    printstop("You got a BlackJack!")
    printstop("You got an instant payout!")
    return bet

  while(player.value < 21): #Your turn playing
    hit_or_stay = ""
    
    while(True):
      hit_or_stay = input("Would you like to hit or stay? ")
      if(hit_or_stay.lower() == "hit" or hit_or_stay.lower() == "stay"):
        break
      else:
        print()
        printstop("Please enter a valid input :)")

    if(hit_or_stay.lower() == "stay"):
      print()
      break
    if(hit_or_stay.lower() == "hit"):
      player.addCard(deck)
      print()
      printstop("You got the ", player.hand[len(player.hand)-1].name)
      printstop("Your hand's value is ", player.getValue())
      
      if(player.value == 21):
        printstop("You got a BlackJack!")
        break
      if(player.value > 21):
        printstop("You busted...")
        return -bet

      if(Justin.value < 17):
        Justin.addCard(deck)
        Justin.getValue()
        printstop("Justin got a new card: ", Justin.hand[len(Justin.hand)-1].name)
      if(Karina.value < 17):
        Karina.addCard(deck)
        Karina.getValue()
        printstop("Karina got a new card: ", Karina.hand[len(Karina.hand)-1].name)
      if(Michelle.value < 17):
        Michelle.addCard(deck)
        Michelle.getValue()
        printstop("Michelle got a new card: ", Michelle.hand[len(Michelle.hand)-1].name)
 
  while(Justin.value < 17): #Continue Justin's turn
    Justin.addCard(deck)
    Justin.getValue()
    printstop("Justin got a new card: ", Justin.hand[len(Justin.hand)-1].name)

  while(Karina.value < 17): #Continue Karina's turn
    Karina.addCard(deck)
    Karina.getValue()
    printstop("Karina got a new card: ", Karina.hand[len(Karina.hand)-1].name)

  while(Michelle.value < 17): #Continue Michelle's turn
    Michelle.addCard(deck)
    Michelle.getValue()
    printstop("Michelle got a new card: ", Michelle.hand[len(Michelle.hand)-1].name)

  #Determine everyone's results
  printstop("Justin reveals his hand's value: ", Justin.getValue())
  if(Justin.value == 21):
    printstop("Justin got a BlackJack!")
  if(Justin.value > 21):
    printstop("Justin busted...")
    Justin.value = -1
  
  printstop("Karina reveals her hand's value: ", Karina.getValue())
  if(Karina.value == 21):
    printstop("Karina got a BlackJack!")
  if(Karina.value > 21):
    printstop("Karina busted...")
    Karina.value = -1

  printstop("Michelle reveals her hand's value: ", Michelle.getValue())
  if(Michelle.value == 21):
    printstop("Michelle got a BlackJack!")
  if(Michelle.value > 21):
    printstop("Michelle busted...")
    Michelle.value = -1
  
  #Continue Dealer's turn
  printstop("The dealer reveals his other card: ", dealer.hand[1].name)
  printstop("The dealer has a value of ", dealer.getValue())
  
  while(dealer.value < player.value and dealer.value < 17): #Dealer's turn playing
    dealer.addCard(deck)
    printstop("The dealer got a new card: ", dealer.hand[len(dealer.hand)-1].name)
    printstop("The dealer has a value of ", dealer.getValue())

  val1, val2, val3, val4 = player.value, Justin.value, Karina.value, Michelle.value

  if(dealer.value == 21):
    printstop("The dealer got a BlackJack...")
    if(dealer.value > val1):
      printstop("You loss...")
      return -bet

  if(dealer.value > 21):
    printstop("The dealer busted...")
    printstop("All remaining player wins!")
    return bet

  if(val1>val2 and val1>val3 and val1>val4):
    printstop("You have the highest hand!")
    printstop("You won!")
    return bet
  
  if(val2>val1 and val2>val3 and val2>val4):
    printstop("Justin had the highest hand...")
    printstop("You loss...")
    return -bet
  
  if(val3>val2 and val3>val1 and val3>val4):
    printstop("Karina had the highest hand...")
    printstop("You loss...")
    return -bet
  
  if(val4>val2 and val4>val3 and val4>val1):
    printstop("Michelle had the highest hand...")
    printstop("You loss...")
    return -bet
  
  if(val1 == val2 or val1 == val3 or val1 == val4 or val1 == dealer.value):
    printstop("You tied...")
    return 0
  
  printstop("The Dealer had the highest hand...")
  printstop("You loss...")
  return -bet

def PlayBlackJack():
  print("* Disclaimer: I don't know all the rules and nuances of BlackJack; certain rules and conditions may not have been implemented *\n")
  time.sleep(5)
  printstop("You decided to go play some BlackJack on a Saturday afternoon")
  printstop("You decided to bring $100 with you")
  printstop("You got to the Casino and sat down at the table")
  printstop("You're playing with Justin, Karina, and Michelle")
  money = 100

  play_again = "yes"
  while(play_again.lower() == "yes"):
    
    while(True):
      try:
        bet = int(input("How much would you like to bet? "))
        if(bet > money):
          printstop("Please put a valid input within your balance :)")
        else:
          break
      except ValueError:
        printstop("Please put a valid input within your balance :)")

    print()
    money += Game(bet)
    if(money == 0):
      return("You've lost all your money...")
    else:
      printstop("You have $" + str(money) + " left")
      play_again = input("Would you like to play again? ")
      print()
      if(play_again.lower() != "yes"):
        break

  return("You walked home with $" + str(money) + " in your pocket...")
