class TheObject:
    def __init__(self, ObjectType, Amount):
        self.Object = ObjectType  # This is a string.
        self.Amount = Amount  # This is an integer.


class Path:
    def __init__(self, NumberSpaces):
        self.NumberSpaces = NumberSpaces  # This is an integer.
        self.BoardArray = []  # This is of type TheObject.

        for _ in range(100):
            self.BoardArray.append(TheObject("", -1))

    def GetNumberSpaces(self):
        return self.NumberSpaces

    def InitialiseData(self, ParameterArray):
        if len(ParameterArray) > self.NumberSpaces:
            return False
        for i in range(len(ParameterArray)):
            self.BoardArray[i] = ParameterArray[i]
        return True

    def ReturnPath(self):
        return_value = ""
        for i in range(self.NumberSpaces):
            return_value += self.BoardArray[i].Object + "-" + str(self.BoardArray[i].Amount) + " "
        return return_value

    def GetPathObject(self, int_index):
        return self.BoardArray[int_index]


ArrayOfObjects = [TheObject("Money", 50), TheObject("Experience", 100),
                  TheObject("Money", 200), TheObject("Experience", 20),
                  TheObject("Experience", 30),]
Path1 = Path(5)
Path1.InitialiseData(ArrayOfObjects)
print(Path1.ReturnPath())
