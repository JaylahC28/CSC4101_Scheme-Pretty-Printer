# Set -- Parse tree node strategy for printing the special form set!

import sys
from Special import Special

class Set(Special):
    def __init__(self):
        pass

    # (set! x 5) on one line like a regular list but always ends the line
    def print(self, t, n, p):
        m = abs(n)
        if not p:
            if n >= 0:
                Special.indent(m)
            sys.stdout.write("(")
        t.getCar().print(-(m + 2))
        Special.printRest(t.getCdr(), m)
        sys.stdout.write("\n")