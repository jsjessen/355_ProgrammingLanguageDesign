#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import sys
import re # regular exressions

import debug

from stack import Stack
import my_dict
import operators

global theStack # operand dictionary, implemented as a list
global sdict # dictionary stack, implemented as a list of dictionaries

# Constants
_PRINT_WIDTH = 80

#============================ Sequencing Operators =============================

def if_():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evaluate(ifcode)
    return None

# NOT IMPLEMENTED !!!
def if_else():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evalLoop(ifcode)
    return None

#=====================================||========================================

def initialize():
    theStack = Stack()
    sdict = Stack()
    sdict.push({})
    return None

def tokenize(fileName, pattern):
    """Given a file name, breaks down the text into meaningful tokens"""
    f = open(fileName, 'r')
    text = f.read()
    f.close()
    return re.findall(pattern, text)

    return None

def evaluate(tokens):
    parenlev = 0
    tok_list = []
    pushList = False
    for t in tokens:

        debug.show("-------------------")
        debug.show("token: {}".format(t))

        if pushList:
            theStack.push(tok_list)
            pushList = False
            tok_list[:] = []
        elif parenlev > 0:
            tok_list.append(t)
            continue
        elif parenlev < 0:
            sys.exit("Error: more '}' than '{'")

        # handle number, push to the stack
        try:
            theStack.push(float(t))
            continue
        except ValueError:
            pass

        # handle stack operations pop, clear, stack
        if hasattr(theStack, t):
            debug.show('Stack Operator')
            getattr(theStack, t)()
            continue

        # handle operator, execute operator
        if hasattr(operators, t):
            debug.show('Operator')
            getattr(operators, t)()
            continue

        if t == '=':
            theStack.peek()
            continue

        # handle def
            # push name and array to the dict stack
        # handle dict
            # define empty dict
            # begin: push dict to the dictionary stack
            # end: pop dict from the dictionary stack
        if hasattr(my_dict, t + '_'):
            debug.show('Dictionary Operator')
            getattr(my_dict, t + '_')()
            continue

        # handle if
            # recursively call “evalLoop” to execute the code array
        if(t == 'if'):
            if_()
            continue

        # handle ifelse
            # recursively call “evalLoop” to execute the code array
        if(t == 'ifelse'):
            ifelse_()
            continue

        if(t == '{'):
            parenlev += 1
            continue

        if(t == '}'):
            parenlev -= 1
            if(parenlev == 0):
                pushList = True
            continue

        sys.exit("Error: Do not recognize '{}'".format(t))

    if parenlev > 0:
        sys.exit("Error: more '{' than '}'")

    return None


if __name__ == '__main__':

    #initialize()
    tokens = ''

    pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'

    for arg in sys.argv[1:]:
        try:
            tokens = tokenize(arg, pattern)
        except IOError:
            sys.exit('Error: Bad input file')

        evaluate(tokens)

        print('=' * _PRINT_WIDTH)
