# Cons -- Parse tree node class for representing a Cons node

from Tree import Node
from Tree import Ident

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):

    # helper function parselist + defines the special forms and their corresponding classes
        from Special import Quote, Lambda, Begin, If, Let, Cond, Define, Set, Regular
        forms = {"quote": Quote, "lambda": Lambda, "begin": Begin, "if": If,
                 "let": Let, "cond": Cond, "define": Define, "set!": Set}
        if self.car.isSymbol() and self.car.name in forms:
            self.form = forms[self.car.name]()
        else:
            self.form = Regular()

    def isPair(self):
        return True

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr

    def setCar(self, a):
        self.car = a
        self.parseList()

    def setCdr(self, d):
        self.cdr = d

    def print(self, n, p=False):
        self.form.print(self, n, p)

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
