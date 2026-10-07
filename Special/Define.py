# Define -- Parse tree node strategy for printing the special form define

import sys
from Special import Special

class Define(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        rest = t.getCdr()
        if rest.isPair() and rest.getCar().isPair():
            Special.printTwoOnFirstLine(t, n, p)
        else:
            m = abs(n)
            if not p:
                if n >= 0:
                    Special.indent(m)
                sys.stdout.write("(")
            t.getCar().print(-(m + 2))
            Special.printRest(rest, m)
            sys.stdout.write("\n")