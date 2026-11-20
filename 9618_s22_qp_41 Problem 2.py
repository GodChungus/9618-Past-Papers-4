class Balloon:
    def __init__(self, defence_item, color):
        self.__health = 100
        self.__defence_item = defence_item
        self.__color = color

    def GetDefenceItem(self):
        return self.__defence_item

    def ChangeHealth(self, value):
        self.__health += value

    def CheckHealth(self):
        return self.__health <= 0