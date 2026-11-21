class Animal:
    def __init__(self, Name, Sound, Size, Intelligence):
        self.Name = Name  # This is a string value.
        self.Sound = Sound  # This is a string value.
        self.Size = Size  # This is an integer, between 1 and 10.
        self.Intelligence = Intelligence  # This is an integer, between 1 and 10.

    def Description(self):
        return (f'The animal\'s name is {self.Name}, it makes a {self.Sound}, its size is'
                f'{self.Size}, and its intelligence level is {self.Intelligence}')