# BoolLit -- Parse tree node class for representing boolean literals

import sys
from Tree import Node

class BoolLit(Node):
    __trueInstance =  None
    __falseInstance = None

    @staticmethod
    def getInstance(val):
        if val:
            if BoolLit.__trueInstance == None:
                BoolLit(True)
            return BoolLit.__trueInstance
        else:
            if BoolLit.__falseInstance == None:
                BoolLit(False)
            return BoolLit.__falseInstance

    def __init__(self, b):
        self.boolVal = b
        if b:
            if BoolLit.__trueInstance != None:
                raise Exception("Class BoolLit is a singleton")
            else:
                BoolLit.__trueInstance = self
        else:
            if BoolLit.__falseInstance != None:
                raise Exception("Class BoolLit is a singleton")
            else:
                BoolLit.__falseInstance = self
        
    def isBool(self):
        return True

    def print(self, n, p=False):
        if n >= 0:
            sys.stdout.write(' ' * n)
        sys.stdout.write('#t' if self.boolVal else '#f')
        if n >= 0:
            sys.stdout.write('\n')

if __name__ == "__main__":
    b = BoolLit.getInstance(True)
    b.print(0)
