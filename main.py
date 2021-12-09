import random
import datetime

e = datetime.datetime.now()

def main(win,lose):
  
# dealing card function - can be used with any deck
# can be modified to pop dealed card from the list - the rest of the code stays the same
  def deal_card():
      card = random.choice(cards)
      return card
#chip class

  class money():
    def __init__(self, chips):
         self.chips = chips
         self.wincase = 1.5  # a gain of 50 % on his bettings

    def wincase(self, bet):  # method to be called when player wins to add his winnings to his account
          if bet <= self.chips:
              self.chips = self.chips + bet * self.wincase
              print(f'You are now left with {self.chips}\n')
              print(f'You have gained an additional of {bet * self.wincase}\n')

    def loosecase(self, bet):  # method to be called when player loses to deduct his loss from his acoount
          if bet <= self.chips:
              self.chips = self.chips - bet
              print(f'You are now left with {self.chips}\n')
              print(f'You lost an amount of {bet}\n')
# calculate_score
  def calculate_score(player_hand, dealer_hand):
      if len(player_hand) == 2:
        if sum_deck(player_hand) == 21:
          player_score = -1
          player_continue = False
          dealer_continue = False
        else:
          player_score = sum_deck(player_hand)
        if sum_deck(dealer_hand) == 21:
          dealer_score = -1
          player_continue = False
          dealer_continue = False
        else:
          dealer_score = sum_deck(dealer_hand)
      else:
        player_score = sum_deck(player_hand)
        dealer_score = sum_deck(dealer_hand)
      if player_score > 21:
        player_score = sum_deck(player_hand) - change_ace_value(player_hand)
      if dealer_score > 21:
        dealer_score = sum_deck(dealer_hand) - change_ace_value(dealer_hand) 
      return player_score, dealer_score

  # check for ace in hand and change 11 to 1
  def change_ace_value(hand):
    correction = 0
    if "A" in hand:
      correction = 10
    return correction

  def sum_deck(deck):
    deck_value = 0
    for card in deck:
      if isinstance(card, int):
        deck_value += card
      else:
        deck_value += card_values.get(card)
    return deck_value

  # final score resolution
  def resolve_score(player_score, dealer_score):
      nonlocal win
      nonlocal lose
      if player_score == -1:
        show_player_score = 21
      else:
        show_player_score = player_score
      if dealer_score == -1:
        show_dealer_score = 21
      else:
        show_dealer_score = dealer_score
      print(f"Your final_hand is {player_hand}.")
      print(f"Your final score is {show_player_score}.\n")
      print(f"Dealer's final hand is {dealer_hand}.")
      print(f"Dealer's final score is {show_dealer_score}.\n")
      # if player or dealer has blackjack - may be changed
      if player_score == -1 or dealer_score == -1:
          if player_score == -1 and dealer_score != -1:
              print("You have Blackjack! You win!")
              win += 1
          if player_score != -1 and dealer_score == -1:
              print(f"Dealer has Blackjack. You lose...")
              lose += 1
          if player_score == -1 and dealer_score == -1:
              print("You both have Blackjack. It is a tie!")
      elif player_score > 21: # if player goes over 21 - loses immediatelly
          print("You went over. You lose...")
          lose += 1
      elif dealer_score > 21:
          print(f"Dealer went over. You win!")
          win += 1
      elif player_score > dealer_score:
          print(f"You win!")
          win += 1
      elif player_score < dealer_score:
          print(f"You lose...")
          lose += 1
      elif player_score == dealer_score:
          print(f"It is a tie!")
      
      return win,lose


  want_to_play = True # loop for another game
  while want_to_play == True:
    # Creating the cards
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    card_values = {"J": 10, "Q": 10, "K": 10, "A": 11}
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0


    player_continue = True
    dealer_continue = True
    beginning = True
    while player_continue == True or dealer_continue == True:
      # two cards are dealed at the beginning without asking user if he wants another - one in 'beginning' one in the normal while loop
      if beginning == True:
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())
        print(f"Dealer's first card is: {dealer_hand[0]}.\n")
        beginning = False
          
      if player_continue == True:
        player_hand.append(deal_card())
      if dealer_continue == True:
        dealer_hand.append(deal_card())
          
      # get the score and resolve the state of the game
      player_score, dealer_score = calculate_score(player_hand,dealer_hand)
      if dealer_score == -1 or player_score == -1:
        player_continue == False 
        dealer_continue = False
    
      # if player_score == 21: # if player has 21 - it is supposed he does not want another card
      #   player_continue = False
        
      if player_score > 21: # player went over
        player_continue = False
        dealer_continue = False
      else:
        if player_continue == True:
          if player_score == -1:
            show_player_score = 21
          else:
            show_player_score = player_score
          print(f"Your current hand is {player_hand} - score is {show_player_score}.")
          go_on = input("Do you want to draw another card? Type 'y' or 'n'.\n")
          if go_on =="y":
            player_continue = True
          else:
            player_continue = False

      if dealer_score > 21: # Dealer went over
        dealer_continue = False
      elif dealer_score < 17 and player_score != -1 and dealer_score != -1: # Dealer must draw below 17 in case nobody has blackjack
        dealer_continue = True
      elif dealer_score >= 17: # Dealer must not draw another card
        dealer_continue = False
            
    win,lose = resolve_score(player_score, dealer_score) # final resolution

    play_another = input("\nDo you want to play again? Type 'y' or 'n'.\n")
    if play_another == "y":
      want_to_play = True
    else:
      want_to_play = False
    
  print(f"player won:{win} times")
  print(f"player lost:{lose} times")
  print("\nBye!n")
  with open('result.txt', 'a') as f:
    f.write("date:  = %s/%s/%s\n" % (e.day, e.month, e.year))
    f.write("time is: = %s:%s:%s\n" % (e.hour, e.minute, e.second))
    f.write(f'  win = {win}\n')
    f.write(f'  lost = {lose}\n')
    f.close()

win=0
lose=0

main(win,lose)    