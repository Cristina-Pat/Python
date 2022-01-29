from typing import Callable
"""
A card has two characters:
first - A, 2-9, T, J, Q, K
second - C: club, D: diamond, H:heart, S:spade
"""

def suit(card: str) -> str: #return the second character of the card
    return card[1]

VALUES = 'A23456789TJQK'

def value(card: str) -> int: #return the value of the card
    for i in range(len(VALUES)):
        if VALUES[i] == card[0]:
            return i + 1 #the output is 1 to 13 for values, not 0-12(i)

def suitValue(card: str) -> tuple:
    return(suit(card), value(card))

def sort(cards: list, key: Callable) -> tuple:
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if key(cards[i]) > key(cards[j]):
               cards[i], cards[j] = cards[j], cards[i]
    print (cards)
    
def insertionSort(cards: list, key: Callable) -> tuple:
    for unsorted in range(1, len(cards)):
        toSort = cards[unsorted]
        theKey = key(toSort) 

        i = unsorted # to start, index where to put card is index where it is now
        while i > 0 and key(cards[i - 1]) > theKey: # for each sorted item larger the one to sort
            cards[i] = cards[i - 1] # shift up to the right
            i-=1 # proceed with the next sorted item on the left
        cards[i] = toSort #set the unsorted item
    print(cards)

#print(suitValue('AS'))

cards = ['2S', 'AS', '2D', 'AD']
insertionSort(cards, suitValue)
#sort(cards, key=suitValue)
#cards.sort(key=suitValue)
#print(cards)
