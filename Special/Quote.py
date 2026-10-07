# Quote -- Parse tree node strategy for printing the special form quote

import sys
from Special import Special
from Special.Regular import Regular

class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    # (quote x) prints as 'x
    def print(self, t, n, p):
        rest = t.getCdr()
        if p or not rest.isPair():
            Regular().print(t, n, p)
            return
        m = abs(n)
        if n >= 0:
            Special.indent(m)
        sys.stdout.write("'")
        rest.getCar().print(-(m + 1))
        if n >= 0:
            sys.stdout.write("\n")
