class Card:
    def __init__(self, number, colour):
        self.__number = number # integer
        self.__colour = colour # string

    def getNumber(self):
        return self.__number

    def getColour(self):
        return self.__colour

class Hand:
    def __init__(self, cards):
        self.__cards = [] # list
        self.__firstCard = 0
        self.__numberCards = 5
    
    def getCard(self, index):
        return self.__hand[index]

    def calculateValue(self):
        score = 0
        score_dictionary = {"red": 5, "blue": 10, "yellow": 15}
        for card in self.__cards:
            score += card.getColour()
        return score

card1 = Card(1, "red")
card2 = Card(2, "red")
card3 = Card(3, "red")
card4 = Card(4, "red")
card5 = Card(5, "red")
card6 = Card(1, "blue")
card7 = Card(2, "blue")
card8 = Card(3, "blue")
card9 = Card(4, "blue")
card10 = Card(5, "blue")
card11 = Card(1, "yellow")
card12 = Card(2, "yellow")
card13 = Card(3, "yellow")
card14 = Card(4, "yellow")
card15 = Card(5, "yellow")

hand1 = [card1, card2, card3, card4, card11]
hand2 = [card12, card13, card14, card15, card6]

player1 = Hand()