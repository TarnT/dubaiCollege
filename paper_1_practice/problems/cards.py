class Card:
    def __init__(self, number, colour):
        self.__number = number # integer
        self.__colour = colour # string

    def getNumber(self):
        return self.__number
    def getColour(self):
        return self.__colour

class Hand:
    def __init__(self, cards, firstCard, numberCards):
        self.__cards = [] # list
        self.__firstCard = firstCard
        self.__numberCards = numberCards
