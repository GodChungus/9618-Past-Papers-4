class TheObject:
    def __init__(self, ObjectType, Amount):
        self.Object = ObjectType
        self.Amount = Amount


class Path:
    def __init__(self, NumberSpaces):
        self.NumberSpaces = NumberSpaces
        self.BoardArray = []

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


