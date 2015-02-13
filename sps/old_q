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


#=====================================||========================================

def initialize():
    stack = Stack()
    sdict = Stack()
    sdict.push({})
    return None

def tokenize(fileName, pattern):
    """Given a file name, breaks down the text into meaningful tokens"""
    f = open(fileName, 'r')
    text = f.read()
    f.close()
    parsed = re.findall(pattern, text)

    #for s in parsed:

    #parsed = list of strings
    #loop through parsed, converting each string into a Token

    return None

def evaluate(tokens):
    p = 0  # control the loop by index p
    while p < len(tokens):
        t = tokens[p]
        p += 1

        # handle number, push to the stack
        try:
            stack.push(float(t))
            continue
        except:
            pass

        # handle operator, execute operator
        try:
            getattr(operators, t)()
            continue
        except:
            pass

        # handle {
        if(t == '{'):
            # push everything between { and } to the stack
            continue

        # handle stack operations pop, clear, stack
        try:
            result = getattr(stack, t)()
            continue
        except:
            pass

        # *** REPACE ALL BELOW WITH THIS??? ***
        try:
            result = getattr(moduleName, t + '_')()
            continue
        except:
            pass
        #****************************************


        # handle def
        if(t == 'def'):
            # push name and array to the dict stack
            continue

        # handle if
        if(t == 'if'):
            # recursively call “evalLoop” to execute the code array
            continue

        # handle ifelse
        if(t == 'ifelse'):
            # recursively call “evalLoop” to execute the code array
            continue

        # handle dict
        if(t == 'dict'):
            # define empty dict
            continue

        if(t == 'begin'):
            # begin: push dict to the dictionary stack
            continue

        if(t == 'end'):
            # end: pop dict from the dictionary stack
            continue

    return None


if __name__ == '__main__':

    initialize()

    pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
    tokens = tokenize(sys.argv[1], pattern)

    evaluate(tokens)
