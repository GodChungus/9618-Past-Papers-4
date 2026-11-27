class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__CurrentSpeed = 0  # This is an integer.
        self.__HorizontalPosition = 0  # This is an integer.
        self.__ID = ID  # This is a string.
        self.__MaxSpeed = MaxSpeed  # This is an integer.
        self.__IncreaseAmount = IncreaseAmount  # This is an integer.

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, NewSpeed):
        self.__CurrentSpeed = NewSpeed

    def SetHorizontalPosition(self, NewPosition):
        self.__HorizontalPosition = NewPosition

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalChange = VerticalChange  # This is an integer.
        self.__MaxHeight = MaxHeight  # This is an integer.
        self.__VerticalPosition = 0  # This is an integer.

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed
