# IntLit -- Parse tree node class for representing integer literals

import sys
from Tree import Node

class IntLit(Node):
    def __init__(self, i):
        self.intVal = i
    
    def isNumber(self):
        return True

    def print(self, n, p=False):
        if n >= 0:
            sys.stdout.write(' ' * n)
        sys.stdout.write(str(self.intVal))
        if n >= 0:
            sys.stdout.write('\n')

if __name__ == "__main__":
    id = IntLit(42)
    id.print(0)
