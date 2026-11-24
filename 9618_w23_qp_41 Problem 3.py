class Character:
    def __init__(self, Name, XPosition, YPosition):
        self.Name = Name  # This is a string.
        self.XPosition = XPosition  # This is an integer.
        self.YPosition = YPosition  # This is an integer.

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, value):
        self.XPosition += value
        if self.XPosition < 0:
            self.XPosition = 0
        elif self.XPosition > 10000:
            self.XPosition = 10000

    def SetYPosition(self, value):
        self.YPosition += value
        if self.YPosition < 0:
            self.YPosition = 0
        elif self.YPosition > 10000:
            self.YPosition = 10000

    def Move(self, input_string):
        if input_string.lower() == "up":
            self.SetYPosition(10)
        elif input_string.lower() == "down":
            self.SetYPosition(-10)
        elif input_string.lower() == "left":
            self.SetXPosition(-10)
        elif input_string.lower() == "right":
            self.SetXPosition(10)
        else:
            print("Invalid input")


class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(self, Name, XPosition)


character1 = Character("Jack", 50, 50)

