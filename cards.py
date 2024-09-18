import random

# generate tuples of card types and faces
# using tuples as they dont need to change
suits = ("Clubs", "Spades", "Hearts", "Diamonds") 
faces = ("Ace", "King", "Queen", "Jack")
numbers = (2, 3, 4 ,5, 6, 7, 8, 9, 10)


def generateDeck():
    """Build a shuffled deck of 52 cards and return it"""
    deck = []

    for suit in suits:
        for value in faces + numbers:
            deck.append(f"{value} of {suit}")
    random.shuffle(deck)
    return deck