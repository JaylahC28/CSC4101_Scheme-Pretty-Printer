# Ident -- Parse tree node class for representing identifiers

import sys
from Tree import Node

class Ident(Node):
    def __init__(self, n):
        self.name = n

    def isSymbol(self):
        return True

    def print(self, n, p=False):
        if n >= 0:
            sys.stdout.write(' ' * n)
        sys.stdout.write(self.name)
        if n >= 0:
            sys.stdout.write('\n')

if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
