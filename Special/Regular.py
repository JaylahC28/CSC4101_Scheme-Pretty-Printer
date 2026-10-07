# Regular -- Parse tree node strategy for printing regular lists

import sys
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    # (a b c) on one line
    def print(self, t, n, p):
        m = abs(n)
        if not p:
            if n >= 0:
                Special.indent(m)
            sys.stdout.write("(")
        t.getCar().print(-(m + 2))
        Special.printRest(t.getCdr(), m)
        if n >= 0:
            sys.stdout.write("\n")