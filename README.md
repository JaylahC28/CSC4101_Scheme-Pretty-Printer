# CSC4101_Scheme-Pretty-Printer
CSC 4101 Project 1: Scheme pretty-printer in Python

Group Members: Jaylah Carter, Claire Bonius
Program Design

The program uses a scanner to convert Scheme input into tokens and a recursive-descent parser to build a tree. The Tree classes represent literals, identifiers, empty lists, and cons cells. The Special classes handle printing rules for special forms. SPP.py connects these components and supports scanner debugging through the -d option.

Testing and Limitations

All 10 tests in the provided server verification suite passed, with 0 formatting failures, 0 failed tests, and 0 reported errors. The factorial example also matched the Java reference output. These results cover the supplied tests; other inputs have not been exhaustively verified. The starter scanner's documented exclusion of the special identifier ... remains.

AI Assistance

Jaylah used ChatGPT to explain the assignment and to plan the division of work.


