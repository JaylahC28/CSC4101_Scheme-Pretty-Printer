# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from Tokens import TokenType
from Tree import Cons, Ident, IntLit, StrLit, BoolLit, Nil

class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        # TODO: write code for parsing an exp
        tok = self.scanner.getNextToken()
        if tok is None:
            return None
        return self._parseToken(tok)

    def parseRest(self):
        # TODO: write code for parsing a rest
        return self._parseListTail(False)
        return None

    # TODO: Add any additional methods you might need
    def _parseToken(self, tok):
        tt = tok.getType()

        if tt == TokenType.LPAREN:
            return self.parseRest()

        elif tt == TokenType.TRUE:
            return BoolLit.getInstance(True)

        elif tt == TokenType.FALSE:
            return BoolLit.getInstance(False)

        elif tt == TokenType.INT:
            return IntLit(tok.getIntVal())

        elif tt == TokenType.STR:
            return StrLit(tok.getStrVal())

        elif tt == TokenType.IDENT:
            return Ident(tok.getName())

        elif tt == TokenType.QUOTE:
            exp = self.parseExp()

            if exp is None:
                self._fail("Expected an expression after quote")

            return Cons(
                Ident("quote"),
                Cons(exp, Nil.getInstance())
            )

        else:
            self._fail("Unexpected token: " + str(tt))

    def _parseListTail(self, allow_dot):
        tok = self.scanner.getNextToken()

        if tok is None:
            self._fail("Unexpected end of input inside a list")

        tt = tok.getType()

        if tt == TokenType.RPAREN:
            return Nil.getInstance()

        if tt == TokenType.DOT:
            if not allow_dot:
                self._fail("A dot must follow a list element")

            tail = self.parseExp()

            if tail is None:
                self._fail("Expected an expression after dot")

            closing = self.scanner.getNextToken()

            if closing is None:
                self._fail("Expected closing parenthesis after dotted tail")

            if closing.getType() != TokenType.RPAREN:
                self._fail("Expected closing parenthesis after dotted tail")

            return tail

        first = self._parseToken(tok)
        rest = self._parseListTail(True)

        return Cons(first, rest)

    def _fail(self, msg):
        self.__error(msg)
        sys.exit(1)

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
