import random
import os

def shuffle_cards(n_decks):
    # Returns a shuffled list of {n_decks} decks of cards 
    # cards are Strings of 0 to 9 then J Q K and A (0 represents 10), and suits
    # C, D, H, S e.g. 0D is 10 of diamonds and KS is king of spades  
    deck = []
    for suit in ('C', 'D', 'H', 'S'):
        for n in range(2, 10):
            # cards 2 to 9
            card = str(n)+suit
            deck.append(card)
        for picture_card in ('0', 'J', 'Q', 'K', 'A'):
            # cards 10 to Ace
            card = picture_card+suit
            deck.append(card)
    decks = []
    for _ in range(n_decks):
        decks += deck
    random.shuffle(decks)
    return decks


def new_game(n_players, n_decks):
    # Starts a new game, returns cards[] which is an array of all the cards
    # cards[0] is the undealt deck, cards[1] is the dealers dealt cards
    # and cards[x] where x > 1 are the players dealt cards
    cards = [shuffle_cards(n_decks)]
    dealer_cards = [cards[0].pop(0), cards[0].pop(0)]
    cards.append(dealer_cards)
    for _player in range (n_players):
        player_cards = [cards[0].pop(0), cards[0].pop(0)]
        cards.append(player_cards)
    return cards

def card_text(code): 
    # Returns the card in long text, e.g. 0S returns 10 ♠
    text = ""
    if code[0] == '0':
        text += '   10'
    elif code[0] == 'A':
        text += '  Ace'
    elif code[0] == 'J':
        text += ' Jack'
    elif code[0] == 'Q':
        text += 'Queen'
    elif code[0] == 'K':
        text += ' King'
    else:
        text += '    ' + code[0]
    if code[1] == 'C':
        text += ' \u2663'
    elif code[1] == 'D':
        text += ' \u2666'
    elif code[1] == 'H':
        text += ' \u2665'
    elif code[1] == 'S':
        text += ' \u2660'
    return text

def show_cards(cards, show_dealer):
    # Displays the currently dealt cards, input is a list of each set of cards
    # as defined in the new_game function.  If show_dealer is False only the first
    # of the dealers cards is displayed, otherwise all dealt cards are shown
    os.system('cls||clear') 
    print("Text based Blackjack game. The cards dealt out are:")
    if not show_dealer:
        card_string = "Dealer:       "
        card_string += card_text(cards[1][0]) + "\t"
        card_string +=  "  ######"
    else:
        card_string = "Dealer ({}):  ".format(score(cards[1]))
        for card in cards[1]:
            card_string += card_text(card) + "\t"
    for player in range(2, len(cards)):
        card_string += "\nPlayer{} ({}): ".format(player-1, score(cards[player]))
        for card in cards[player]:
            card_string += card_text(card) + "\t"
    card_string += "\n"
    print(card_string)
    

def score(cards):
    # Returns the total of the card list input.  Ace counts as 11 unless the total
    # greater than 21 then it counts as 1.
    total = 0
    for card in cards:
        if card[0] in ('0', 'J', 'Q', 'K'):
            total += 10
        elif card[0] == 'A':
            # Initially sets all aces to 11, checked in next loop if total >21
            total += 11
        else:
            total += int(card[0])
    for card in cards:
        if total > 21 and card[0] == 'A':
            # If the total is over 21 and the card is an ace it is set to score 1
            # instead of the initial 11 set above. Repeated for all dealt cards
            # e.g. cards (2, A, A, A) would score (2 + 1 + 1 + 11 = 15)
            total -= 10
    return total

def main():
    # Runs the game and calculates the result 
    os.system('cls||clear')
    while True:
        try:
            num_players = int(input("Welcome to the text based Blackjack game. \nEnter the number of players (1-10): "))
            if num_players > 10 or num_players < 1:
                input("Invalid number input")
            else:
                break
        except:
            continue
    num_decks = 6

    while True:
        scores = []        
        cards = new_game(num_players, num_decks)
        show_cards(cards, False)
        for player in range(2, num_players+2):
            # For each player the current score is displayed and a choice is given to
            # hit or stand
            player_score = score(cards[player])
            if player_score == 21:
                input("\nPlayer{} BLACKJACK! press enter to continue ".format(player-1))
                # Higher score than a non blackjack 21, NB. non blackjack card scores of >21 are set to -1 below
                player_score = 22
            else:   
                while player_score < 21 and player_score > 0:
                    show_cards(cards, False)
                    score_text = "({}):  Hit (h) or Stand (s)?".format(player_score)
                    choice = input("\nPlayer{} {} ".format(player-1, score_text)).lower()
                    if choice == 'y' or choice == 'h':
                        cards[player].append(cards[0].pop())
                        player_score = score(cards[player])
                        show_cards(cards, False)
                        if player_score == 21:
                            input("\n21! press enter to continue")
                        if player_score > 21:
                            input("\nBust! press enter to continue")
                            player_score = -1 # Even lower than the dealer busting (0)
                    elif choice == 'n' or choice == 's':
                        break
                    else:
                        input("Invalid input '{}'".format(choice))
            scores.append(player_score)
        dealer_score = score(cards[1])        
        if dealer_score == 21:
            show_cards(cards, True)
            print("Dealer Blackjack!")
            # Higher score than a non blackjack 21, NB. non blackjack card scores of >21 are set to 0 before comparison
            dealer_score = 22            
        else:
            while dealer_score < 17:
                cards[1].append(cards[0].pop())
                dealer_score = score(cards[1])
            show_cards(cards, True)
            if dealer_score > 21:
                print("\nDealer Bust!")
                dealer_score = 0  # Only thing that looses to the dealer busting is the player busting (-1)
            else:                
                print("\nDealer ({})".format(dealer_score))
        for player in range(num_players):
            if scores[player] == dealer_score:
                result_text = "Draw"
            elif scores[player] > dealer_score:
                result_text = "Wins!"
            else:
                result_text = "Looses"
            print("Player{} {}".format(player+1, result_text))
        choice = input("\nDo you want to play again? (y/n) ")
        if choice != 'y':
            break

main()