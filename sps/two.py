#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import sys
import re # regular exressions

global stack # operand dictionary, implemented as a list
global sdict # dictionary stack, implemented as a list of dictionaries

#_PRINT_WIDTH = 80
#
#debugging = True  # view debugging output
#debugging = False  # hide debugging output

#=========================== Mathematical Operators ============================

# (2 3 add) = (2 + 3) = 5
#
#     |---|
#     |add|
#     |---|
#     | 3 |
#     |---|     |---|
#     | 2 |     | 5 |
#     |---| ==> |---|
#     |...|     |...|
#     |___|     |___|
def add():
    """Addition"""
    if len() >= 2: # stack has at least 2 items
        push(isNum(pop()) + isNum(pop()))
    return None

# (8 5 sub) = (8 - 5) = 3
#
#     |---|
#     |sub|
#     |---|
#     | 5 |
#     |---|     |---|
#     | 8 |     | 3 |
#     |---| ==> |---|
#     |...|     |...|
#     |___|     |___|
def sub():
    """Subtraction"""
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) - isNum(pop()))
    return None

# (2 3 mul) = (2 * 3) = 6
#
#     |---|
#     |mul|
#     |---|
#     | 3 |
#     |---|     |---|
#     | 2 |     | 6 |
#     |---| ==> |---|
#     |...|     |...|
#     |___|     |___|
def mul():
    """Multiplication"""
    if len() >= 2: # stack has at least 2 items
        push(isNum(pop()) * isNum(pop()))
    return None

# (6 4 div) = (6 / 4) = 1.5
#
#     |---|
#     |div|
#     |---|
#     | 4 |
#     |---|     |---|
#     | 6 |     |1.5|
#     |---| ==> |---|
#     |...|     |...|
#     |___|     |___|
def div():
    """ Divide the second number on the stack by the top number on the stack """
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) / isNum(pop()))
    return None

# (6 4 idiv) = (6 / 4) = 1
#
#     |-----|
#     |idiv |
#     |-----|
#     |  4  |
#     |-----|     |---|
#     |  6  |     | 1 |
#     |-----| ==> |---|
#     | ... |     |...|
#     |_____|     |___|
def idiv():
    """Divide the second number on the stack by the top number on the stack"""
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) // isNum(pop()))
    return None

# (2 neg) = (-2) = -2
#
#     |---|
#     |neg|
#     |---|     |----|
#     | 2 |     | -2 |
#     |---| ==> |----|
#     |...|     |....|
#     |___|     |____|
def neg():
    """Negate the top number on the stack"""
    if len() >= 1:
        push(-isNum(pop()))


#============================ Comparison Operators =============================

def eq():
    """Equal to"""
    if len() >= 2:
        if isNum(pop()) == isNum(pop()):
            push('true')
        else:
            push('false')
    return None

def lt():
    """Less than"""
    if len() >= 2:
        if isNum(pop()) > isNum(pop()): # (2 4 lt) = (2 < 4) = (4 > 2)
            push('true')
        else:
            push('false')
    return None

def gt():
    """Greater than"""
    if len() >= 2:
        if isNum(pop()) < isNum(pop()): # (4 2 gt) = (4 > 2) = (2 < 4)
            push('true')
        else:
            push('false')
    return None


#============================== Boolean Operators ==============================

def and_():
    """ ? """
    if len() >= 2:
        if isBool(pop()) and isBool(pop()):
            push('true')
        else:
            push('false')
    return None

def or_():
    """ ? """
    if len() >= 2:
        if isBool(pop()) or isBool(pop()):
            push('true')
        else:
            push('false')
    return None

def not_():
    """ ? """
    if len() >= 2:
        if isBool(pop()) not isBool(pop()):
            push('true')
        else:
            push('false')
    return None


#============================ Sequencing Operators =============================

def if_():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evalLoop(ifcode)
    return None

# NOT IMPLEMENTED !!!
def if_else():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evalLoop(ifcode)
    return None


#================================= Checks ======================================

def isNum(item):
    """Check if the item is a number"""
    if isinstance(item, float):
        return item
    else:
        err("Variable not a float.")

def isDict(item):
    """Check if the item is a dictionary"""
    if isinstance(item, dict):
        return item
    else:
        err("Variable not a dictionary.")

def isString(item):
    """Check if the item is a string"""
    if isinstance(item, str):
        return item
    else:
        err("Variable not a string.")

def isCode(item):
    """Check if the item is code"""
    if isinstance(item, list):
        return item
    else:
        err("Variable not code.")

def isBool(item):
    """Check if the item is a boolean"""
    if isinstance(item, bool):
        return item
    else:
        err("Variable not a boolean.")


#============================= Stack Operators =================================

 class Stack:
     def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        """Push an item onto the stack"""
        self.items.append(item)      # append new item to the end of list
        return None

    def pop(self):
        """Pop the first item off the stack and return it"""
        if not stack:           # If the stack is empty
            err("pop: stack is empty")
            return None
        else:                   # The stack has at least one item
            return self.items.pop()  # Return the last item of the stack

    # Call this function when you encounter "len"
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

    def clear(self):
        """Empty the stack"""
        self.items[:] = []
        return None

    def dup(self):
        """Duplicate the top item of the stack"""
        self.items.push(stack[-1])
        return None

    def exch(self):
        """Exchange the top two stack values"""
        first, second = pop(), pop()
        push(first)
        push(second)
        return None

    # Call this function when you encounter "stack"
    def print(self):
    """Display the contents of the stack, without modifying it"""
    for item in reversed(self.items):
        print(item)
    return None

    # Call this function when you encounter '='
    def peek(self):
        """Pop the top item off of the stack and print it"""
        print(self.items.pop())
        return None

#=====================================||========================================
#(Normally Postscript uses a dict operator requiring one operand. Our SPS has the dictz operator with zero operands. You can run regular postscript code in your interpreter if you prefix the Postscript code by /dict {pop dictz} def, to provide a sensible definition for the missing dict operation.)
def dictz():
    """ ? """
    return None

# begin requires one dictionary operand on the operand stack
def begin(in_dict):
    """ ? """
    return None

# end has no operands
def end():
    """ ? """
    return None

# The  def operator defines a name.  def requires its two operands to be on the stack:
#    name (constant) to be defined and
#    the value to which it will be bound
def def_(name, value):
    """ ? """
    return None

#• SPS dictionaries; modularizing the dictionaries means implementing functions that operate on dictionary to determine whether it contains an entry for a particular name, to retrieve the value associated with a particular name, and to enter a new (name, value) pair.

#• the dictionary stack: as with the operand stack, implement functions to push and pop values on the dictionary stack, check whether it is empty, etc.

#=====================================||========================================

def initialize():
    stack = []
    sdict = [{}]
    return None

def tokenize(fileName, pattern):
    """Given a file name, breaks down the text into meaningful tokens"""
    text = open(fileName).read()
    return re.findall(pattern, text)

def evaluate(tokens):
    p = 0  # control the loop by index p
    while p < len(tokens):
        t = tokens[p]
        p += 1

        # handle number, push to the stack
        # handle operator, execute operator
        # handle {
        # push everything between { and } to the stack
        # handle stack operations pop, clear, stack
        # handle def
        # push name and array to the dict stack
        # handle if
        # recursively call “evalLoop” to execute the code array
        # handle ifelse
        # recursively call “evalLoop” to execute the code array
        # handle dict
        # define empty dict
        # begin: push dict to the dictionary stack
        # end: pop dict from the dictionary stack

    return None


if __name__ == '__main__':

    initialize()

    pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
    tokens = tokenize(sys.argv[1], pattern)

    evaluate(tokens)
