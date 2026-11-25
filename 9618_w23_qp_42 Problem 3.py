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

    def SetIntelligence(self, value):
        self.Intelligence = value

    def Learn(self):
        self.Intelligence *= 1.1

    def ReturnAge(self):
        return 2023 - self.DateOfBirth.year


class MagicCharacter(Character):
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed, Element):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.Element = Element

    def Learn(self):
        if self.Element.lower() == "fire" or self.Element.lower() == "water":
            self.Intelligence *= 1.2
        elif self.Element.lower() == "earth":
            self.Intelligence *= 1.3
        else:
            self.Intelligence *= 1.1


FirstCharacter = Character("Royal", datetime.date(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print(f'The name of the character is {FirstCharacter.GetName()}. They are {FirstCharacter.ReturnAge()} years old. Moreover, '
      f'their intelligence level is {FirstCharacter.GetIntelligence()}.')
