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
            return i + 1 #teh output is 1 to 13 for values, not 0-12(i)

def suitValue(card: str) -> tuple:
    return(suit(card), value(card))


print(suitValue('AS'))

cards = ['2S', 'AS', '2D', 'AD']
cards.sort(key=suitValue)
print(cards)
