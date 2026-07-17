# this program uses a dictionary
# as a deck of playing cards

def main():
    #creates deck of cards
    deck = create_deck()

    # gets number of cards to deal
    num_cards = int(input('How many cards should I deal?'))

    #deals cards
    deal_cards(deck, num_cards)
    # the create deck function returns a
    # dictionary representing a deck of cards
def create_deck():
    # creates a dictionary with each card
    # and its value stored as key-value pairs
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,

            'Ace of hearts':1, '2 of hearts':2, '3 of hearts':3,
            '4 of hearts':4, '5 of hearts':5, '6 of hearts':6,
            '7 of hearts':7, '8 of hearts':8, '9 of hearts':9,
            '10 of hearts':10, 'Jack of hearts':10,
            'Queen of hearts':10, 'King of hearts': 10,

            'Ace of clubs':1, '2 of clubs':2, '3 of clubs':3,
            '4 of clubs':4, '5 of clubs':5, '6 of clubs':6,
            '7 of clubs':7, '8 of clubs':8, '9 of clubs':9,
            '10 of clubs':10, 'Jack of clubs':10,
            'Queen of clubs':10, 'King of clubs': 10,

            'Ace of diamonds':1, '2 of diamonds':2, '3 of diamonds':3,
            '4 of diamonds':4, '5 of diamonds':5, '6 of diamonds':6,
            '7 of diamonds':7, '8 of diamonds':8, '9 of diamonds':9,
            '10 of diamonds':10, 'Jack of diamonds':10,
            'Queen of diamonds':10, 'King of diamonds': 10,}
    
    #returns deck
    return deck

# the deals_cards function deals a specified
# number of cards from the deck

def deal_cards(deck, number):
    # initialize accumulator for the hand
    hand_value = 0

    # makes sure the number of cards dealt is not
    # greater than the number of cards in the deck
    if number > len(deck):
        number = len(deck)

    # deals cards and accumulates their value
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value =+ value
        
    # displays the value of the hand dealt
    print('The value of this hand is: ', hand_value)

#calls main function
main()
