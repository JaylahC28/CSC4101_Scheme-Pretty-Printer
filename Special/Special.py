# Special -- Parse tree node strategy for printing special forms

import sys
from abc import ABC, abstractmethod

# There are several different approaches for how to implement the Special
# hierarchy.  We'll discuss some of them in class.  The easiest solution
# is to not add any fields and to use empty constructors.

class Special(ABC):
    @abstractmethod
    def print(self, t, n, p):
        pass

    @staticmethod
    def indent(n):
        sys.stdout.write(' ' * abs(n))

    @staticmethod
    def printBody(t, n):
        while t.isPair():
            t.getCar().print(n)
            t = t.getCdr()
        if not t.isNull():
            Special.indent(n)
            sys.stdout.write(". ")
            t.print(-n)
            sys.stdout.write("\n")
        Special.indent(n - 2)
        sys.stdout.write(")\n")

    @staticmethod
    def printTwoOnFirstLine(t, n, p):
        m = abs(n)
        if not p:
            if n >= 0:
                Special.indent(m)
            sys.stdout.write("(")
        rest = t.getCdr()
        if not rest.isPair():
            t.getCar().print(-(m + 2))
            Special.printRest(rest, m)
            if n >= 0:
                sys.stdout.write("\n")
            return
        t.getCar().print(-(m + 2))
        sys.stdout.write(" ")
        rest.getCar().print(-(m + 2))
        sys.stdout.write("\n")
        Special.printBody(rest.getCdr(), m + 2)

    @staticmethod
    def printKeywordOnFirstLine(t, n, p):
        m = abs(n)
        if not p:
            if n >= 0:
                Special.indent(m)
            sys.stdout.write("(")
        t.getCar().print(-(m + 2))
        sys.stdout.write("\n")
        Special.printBody(t.getCdr(), m + 2)

    @staticmethod
    def printRest(t, m):
        while t.isPair():
            sys.stdout.write(" ")
            t.getCar().print(-(m + 2))
            t = t.getCdr()
        if not t.isNull():
            sys.stdout.write(" . ")
            t.print(-(m + 2))
        sys.stdout.write(")")