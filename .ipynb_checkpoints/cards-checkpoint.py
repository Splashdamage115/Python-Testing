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

def cards_dict():
    """
    Returns a shuffled dictionary of cards using "name" "value" pairs
    """
    cards = {}
    for suit in suits:
        for card in faces + numbers:
            value = 0
            if card == "Ace":
                value = [1,11]
            elif card in ["Jack", "Queen", "King"]:
                value = 10
            else:
                value = card
            name = f"{card} of {suit}"
            cards.update({name: value})
        
    cards_list = list(cards.items())
    random.shuffle(cards_list)
    return dict(cards_list)