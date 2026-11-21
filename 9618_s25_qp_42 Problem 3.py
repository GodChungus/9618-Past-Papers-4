class Animal:
    def __init__(self, Name, Sound, Size, Intelligence):
        self.Name = Name  # This is a string value.
        self.Sound = Sound  # This is a string value.
        self.Size = Size  # This is an integer, between 1 and 10.
        self.Intelligence = Intelligence  # This is an integer, between 1 and 10.

    def Description(self):
        return (f'The animal\'s name is {self.Name}, it makes a {self.Sound}, its size is'
                f'{self.Size}, and its intelligence level is {self.Intelligence}')


class Parrot(Animal):
    def __init__(self, WingSpan, NumberWords, Name, Sound, Size, Intelligence):
        Animal.__init__(self, Name, Sound, Size, Intelligence)
        self.WingSpan = WingSpan  # This is an integer.
        self.NumberWords = NumberWords  # This is an integer.

    def Description(self):
        return (f'The animal\'s name is {self.Name}, it makes a {self.Sound}, its size is'
                f'{self.Size}, and its intelligence level is {self.Intelligence}. It has a '
                f'wingspan of {self.WingSpan}cm and can say {self.NumberWords} words.')


class Wolf(Animal):
    def __init__(self, TerritorySize, Name, Sound, Size, Intelligence):
        Animal.__init__(self, Name, Sound, Size, Intelligence)
        self.TerritorySize = TerritorySize  # This is an integer.

    def SetTerritorySize(self, value):
        self.TerritorySize += value

    def Description(self):
        return (f'The animal\'s name is {self.Name}, it makes a {self.Sound}, its size is'
                f'{self.Size}, and its intelligence level is {self.Intelligence}. Its'
                f'territory is {self.TerritorySize} square miles.')


chewie = Parrot(30, 29, "Chewie", "Squawk", 1, 10)
nightEyes = Wolf(100, "Nighteyes", "Howl", 8, 7)
copper = Animal("Copper", "Neigh", 10, 6)
