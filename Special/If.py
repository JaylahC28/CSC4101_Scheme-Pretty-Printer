# If -- Parse tree node strategy for printing the special form if

from Special import Special

class If(Special):
    def __init__(self):
        pass

# first two elements of the list are printed on the first line, and the rest indented below
    def print(self, t, n, p):
        Special.printTwoOnFirstLine(t, n, p)


