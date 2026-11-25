import datetime


class Character:
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        self.CharacterName = CharacterName
        self.DateOfBirth = DateOfBirth
        self.Intelligence = Intelligence
        self.Speed = Speed

    def GetIntelligence(self):
        return self.Intelligence

    def GetName(self):
        return self.CharacterName
