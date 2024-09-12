from DeckOfCards import *

#Keeping track of scores and aces(so we can code 1 or 11 logic)
def score_calculation(hand):
    score = 0
    ace_count = 0
# calculate the user's hand score
    for card in hand:
        score += card.val
        if card.face == 'Ace':
            ace_count -=1
#Changes an ace from a 11 to 1 if bust
    while score > 21 and ace_count:
        score -= 10
        ace_count -=1
    return score


#Visual interface (mostly ties back into main game)
def visual_hand(hand, name):
    counter = 1
    for card in hand:
        print(f"Card number {counter} is: {card}")
        counter +=1
        
    print(f"Total score is: {score_calculation(hand)}")
    
# Main game function
def main_game():
    print("Welcome to Black Jack")
    print()

#Shuffling occurs here, print() is used for spacing purposes

    while True:
        deck = DeckOfCards()
        print("Deck before shuffled:")
        deck.print_deck()
        print()
        deck.shuffle_deck()
        print("Deck after shuffled:")
        deck.print_deck()
        print()

#Starts by giving user and dealer 2 cards
   
        user_hand = [deck.get_card(), deck.get_card()]
        dealer_hand = [deck.get_card(), deck.get_card()]
        
        visual_hand(user_hand, "Your")

#Game conditions (ie.bust, hit, hold)

        while True:
            user_score = score_calculation(user_hand)
            if user_score > 21:
                print("Busted, you lost :(")
                break
            
            hit = input("Would you like a hit? (y/n): ")
            if hit == 'y':
                user_hand.append(deck.get_card())
                visual_hand(user_hand, "Your")
            else:
                break
        
        if user_score <= 21:
            print("Dealer's turn...")
            visual_hand(dealer_hand, "Dealer's")

            dealer_score = score_calculation(dealer_hand)
            while dealer_score < 17:
                dealer_hand.append(deck.get_card())
                dealer_score = score_calculation(dealer_hand)
                visual_hand(dealer_hand, "Dealer's")

            if dealer_score > 21:
                print("Dealer busted! You win!")
            elif user_score > dealer_score:
                print("Your score is higher, you win!")
            else:
                print("Your score is lower, you lose!")

        another_game = input("Another game? (y/n): ")
        if another_game != 'y':
            break

# Entry point for the program (cleaner than more if true statements)

        
if __name__ == "__main__":
    main_game()       


