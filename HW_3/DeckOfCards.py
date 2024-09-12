import random
#Your program will create a DeckOfCards object using your DeckOfCards class.  This object will contain a list of 52 Card objects. The DeckOfCards Class already contains a shuffle_deck() function to shuffle a new deck, and a get_card() function returns the next card in the deck (card at index 0 in the list).  

#Your program must print the deck of cards before, and after, they are shuffled (I want to see they are being shuffled properly). 
#Your program must also be able to correctly score the card based on the suit.  i.e...

 #“2 of Spades” = 2 points
#“3 of Spades" = 3 points
#“9 of Spades" = 9 points
#“10 of Spades" = 10 points
#“Jack of Spades" = 10 points
#“Queen of Spades" = 10 points
#“King of Spades" = 10 points
#“Ace of Spades" = 11 points or 1 point (Details on how to implement this below (it's actually not hard))


class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)


class DeckOfCards():
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.play_idx = 0
        
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("---")
        
    def get_card(self):
        if self.play_idx < len(self.deck):
            card = self.deck[self.play_idx]
            self.play_idx += 1
            return card
        return None
    
