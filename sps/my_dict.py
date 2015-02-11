#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

import stack

class DictStack(stack.PostScriptStack):
    """Describe stack class"""
    def __init__(self):
         self.items = {}

    # Call this function when you encounter "stack"
    def print(self):
        """Display the contents of the stack, without modifying it"""
        for item in reversed(self.items):
            print(item)
        print('=======================')
        return None

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
