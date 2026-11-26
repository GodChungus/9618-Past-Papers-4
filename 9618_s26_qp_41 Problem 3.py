class TheObject:
    def __init__(self, ObjectType, Amount):
        self.Object = ObjectType # This is a string.
        self.Amount = Amount # This is an integer.


class Path:
    def __init__(self, NumberSpaces):
        self.NumberSpaces = NumberSpaces # This is an integer.
        self.BoardArray = [] # This is of type TheObject.

        for _ in range(100):
            self.BoardArray.append(TheObject("", -1))

    def GetNumberSpaces(self):
        return self.NumberSpaces

    def InitialiseData(self, ParameterArray):
        if len(ParameterArray) > len(self.BoardArray):
            return False
        for i in range(len(ParameterArray)):
            self.BoardArray[i] = ParameterArray[i]
        return True


