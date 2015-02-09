#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import sys
import re #regular exressions

# Used this value because it's less than 80 and
# aligns nicely with both the histogram and digraph output.
_PRINT_WIDTH = 78

#debugging = True  # view debugging output
debugging = False  # hide debugging output


#================================= Test/Debug ==================================

def debug(*s):
    """Print but only when debugging"""
    if debugging:
        print(*s)


def test(function, outputs, *inputs):
    """Test function with inputs and compare actual outputs with expected"""
    result = True

    for o, i in zip(outputs, *inputs):
        actual = function(*i)
        if(actual != o):
            result = False
            # Create visual seperation between failures
            debug('=' * _PRINT_WIDTH)
            debug(function.__name__ + "(" +  str(i).strip('[]()') + ")")
            debug('-' * _PRINT_WIDTH)
            debug("Actual:")
            debug(actual)
            debug('.' * _PRINT_WIDTH)
            debug("Expected:")
            debug(o)

    # Create visual seperation between tested functions, if there is need
    if(result == False):
        debug(('#' * _PRINT_WIDTH) + '\n')

    return result

# read lines from input file
# tokenize
# classify each token


# class stack
# class dict

# Stack Operators
# Implement stack with a python list
# NOT IMPLEMENTED !!!
def spush():
    """Push an item onto the stack"""
    return 0

# NOT IMPLEMENTED !!!
def spop():
    """Pop the first item off the stack and return it"""
    return 0

# Mathematical Operators
def add():
    """ ? """
    spush(spop() + spop())

# Check that spop() calls are evaluated in the correct order !!!
def sub():
    """ ? """
    #secondOperand = spop()
    #firstOperand = spop()
    #spush(firstOperand > second operand)
    spush(spop() - spop())

def mul():
    """ ? """
    spush(spop() * spop())

# Check that python and PostScript agree on divide type !!!
def div():
    """ ? """
    spush(spop() / spop())

# Comparison Operators
# Check ordering !!!
def eq:
    """ ? """
    spush(spop() == spop())

def lt:
    """ ? """
    spush(spop() < spop())

def gt:
    """ ? """
    spush(spop() > spop())

# built-in operators on boolean values: and, or, not; these take boolean operands only.
# Boolean Operators
# Operands must be boolean values, else error
# NOT IMPLEMENTED !!!
def _and():
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _or():
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _not():
    """ ? """
    return 0

#
# • * built-in sequencing operators: if, ifelse; make sure that you understand the order of the
# Sequencing Operators
# NOT IMPLEMENTED !!!
def _if():
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _ifelse():
    """ ? """
    return 0

# • * stack operators: dup, exch, pop
# Stack Operators
# NOT IMPLEMENTED !!!
def _dup():
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _exch():
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _pop():
    """ ? """
    return 0

# • * dictionary creation operator: dictz; takes no operands
#(Normally Postscript uses a dict operator requiring one operand. Our SPS has the dictz operator with zero operands. You can run regular postscript code in your interpreter if you prefix the Postscript code by /dict {pop dictz} def, to provide a sensible definition for the missing dict operation.)
# NOT IMPLEMENTED !!!
def dictz():
    """ ? """
    return 0

# • * dictionary stack manipulation operators: begin, end. begin requires one dictionary operand on the operand stack; end has no operands.
# NOT IMPLEMENTED !!!
def _begin(in_dict):
    """ ? """
    return 0

# NOT IMPLEMENTED !!!
def _end():
    """ ? """
    return 0

# • * name definition operator: def. This requires two operands, a name and a value.

# NOT IMPLEMENTED !!!
def _def(name, value):
    """ ? """
    return 0

# • * stack printing operator (prints contents of stack without changing it): stack

# NOT IMPLEMENTED !!!
def _stack(name, value):
    """ ? """
    return 0

# • * top-of-stack printing operator (pops the top element of the stack and prints it): =

# NOT IMPLEMENTED !!!
def _=(name, value):
    """ ? """
    return 0

#For correct SPS programs your interpreter should produce the same output (stack contents) as produced by a PostScript interpreter. The code for this assignment will be used as a starting place for a future assignment. Therefore, it is important to do a good job of organizing and documenting your code so it can be easily understood and modified several weeks later. In particular you must modularize the parts of your code that implement the following components of the SPS abstract machine (for the Monday, February 9 deadline):

#• the operand stack; modularlizing this means having operators to push and pop values so that elsewhere in your code you don’t have to worry about the details of the stack implementation, or checking that the stack contains at least one value when you want to do a pop.

#• SPS dictionaries; modularizing the dictionaries means implementing functions that operate on dictionary to determine whether it contains an entry for a particular name, to retrieve the value associated with a particular name, and to enter a new (name, value) pair.

#• the dictionary stack: as with the operand stack, implement functions to push and pop values on the dictionary stack, check whether it is empty, etc.

#• IMPORTANT NOTE: implementing the functions required for the preliminary February 9 due date requires that you also design and implement the operand stack, dictionaries, and the dictionary stack.

open(sys.argv[1]).readlines()

