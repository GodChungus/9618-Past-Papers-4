# What a disgusting problem.


class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number  # This is an integer.
        self.__Colour = Colour  # This is a string.

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []  # This is an array with 10 values of type Card.
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0  # This is an integer.
        self.__NumberCards = 5  # This is an integer.

    def GetCard(self, index_parameter):
        return self.__Cards[index_parameter]


def CalculateValue(player_hand):
    score = 0
    for i in range(5):
        if player_hand.GetCard(i).GetColour() == 'red':
            score += player_hand.GetCard(i).GetNumber()+5
        elif player_hand.GetCard(i).GetColour() == 'blue':
            score += player_hand.GetCard(i).GetNumber()+10
        elif player_hand.GetCard(i).GetColour() == 'yellow':
            score += player_hand.GetCard(i).GetNumber()+15
        else:
            pass
    return score



card1 = Card(1, 'red')
card2 = Card(2, 'red')
card3 = Card(3, 'red')
card4 = Card(4, 'red')
card5 = Card(5, 'red')
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

player_1 = Hand(card1, card2, card3, card4, card11)
player_2 = Hand(card12, card13, card14, card15, card6)

if CalculateValue(player_1) > CalculateValue(player_2):
    print("Player 1 won")
elif CalculateValue(player_1) < CalculateValue(player_2):
    print("Player 2 won")
else:
    print("Draw")
