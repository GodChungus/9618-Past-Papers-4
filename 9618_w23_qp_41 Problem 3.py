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