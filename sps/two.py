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

import ps_stack
import ps_dict

global stack # operand dictionary, implemented as a list
global dicts # dictionary stack, implemented as a list of dictionaries

# Constants
_PRINT_WIDTH = 80

#============================ Sequencing Operators =============================

#   condition (if condition: code)
#   {code}
# if
#
#     |-----------|
#     |    if     |
#     |-----------|
#     |   code    |
#     |-----------|
#     | condition |
#     |-----------|
#
# requires 2 objects on stack
#   a boolean value
#   one executable array
def if_():
    """Execute code array if the condition is true"""
    if stack.size() >= 2:
        ifcode = isCode(stack.pop()) # Make sure it is code (a list)
        if chBool(stack.pop()):
            evaluate(ifcode)
    else:
        debug.err("not enough items on the stack")
    return None

#   condition   (if condition: trueCode; else: falseCode)
#   {trueCode}
#   {falseCode}
# ifelse
#
#     |-----------|
#     |  ifelse   |
#     |-----------|
#     | falseCode |
#     |-----------|
#     | trueCode  |
#     |-----------|
#     | condition |
#     |-----------|
#
# requires 3 objects on stack
#   a boolean value
#   two executable arrays
def ifelse_():
    """Execute first code array if the condition is true and the second if it is false"""
    if stack.size() >= 3:
        trueCode = isCode(stack.pop()) # Make sure it is code (a list)
        falseCode = isCode(stack.pop()) # Make sure it is code (a list)
        if chBool(stack.pop()):
            evaluate(trueCode)
        else:
            evaluate(falseCode)
    else:
        debug.err("not enough items on the stack")
    return None

#=====================================||========================================

    # begin requires one dictionary operand on the operand stack
    def begin(in_dict):
        """Create a new dictionary on the top of the dictionary stack"""
        dicts.push(Dict())
        return None

    # end has no operands
    def end():
        """Remove the a dictionary from the top of the dictionary stack"""
        dicts.pop()
        return None

#=====================================||========================================

def initialize():
    global stack
    global dicts
    stack = ps_stack.PostScriptStack()
    dicts = ps_stack.PostScriptStack()
    dicts.push(ps_dict.PostScriptDict())
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
    codeBlock = []
    for t in tokens:

        debug.show("-------------------")
        debug.show("token: {}".format(t))

        # handle {
        if t == '{':
            parenlev += 1
            continue

        # handle }
        if t == '}':
            parenlev -= 1
            if(parenlev == 0):
                stack.push(codeBlock)
                codeBlock = []
            elif(parenlev < 0):
                sys.exit("Error: too many '}' or not enough '{'")
            continue

        # if in {}, add to code block list
        # Important: After handling of '}'
        if parenlev > 0:
            codeBlock.append(t)
            continue

        # handle number, push to the stack
        try:
            stack.push(float(t))
            continue
        except ValueError:
            pass

        if (t == 'true') or (t == 'false'):
            stack.push(t)

        if t == '=':
            print(stack.pop())
            continue

        # handle if
        if t == 'if':
            if_()
            continue

        # handle ifelse
        if t == 'ifelse':
            ifelse_()
            continue

        if t == 'def':
            stack.exch()
            dicts.add(stack.pop(), stack.pop())

        if t == 'begin':
            begin()
            continue

        if t == 'end':
            end()
            continue

        # handle string literals
        if t[0] == '/':
            stack.push(t)
            continue

        # handle stack operations pop, clear, stack
        # handle operator, execute operator
        if hasattr(stack, t):
            debug.show('Stack Operator')
            getattr(stack, t)()
            continue
        elif hasattr(stack, t + '_'):
            debug.show('Stack Operator')
            getattr(stack, t + '_')()
            continue

        # handle def
        # handle dict
        if hasattr(dicts, t):
            debug.show('Dictionary Operator')
            getattr(dicts, t)()
            continue
        elif hasattr(dicts, t + '_'):
            debug.show('Dictionary Operator')
            getattr(dicts, t + '_')()
            continue

        # search for tok in dicts, starting with top dict and moving downward
        # if found, use key to get value, push value onto stack

        sys.exit("Error: Do not recognize '{}'".format(t))

    if parenlev > 0:
        sys.exit("Error: too many '{' or not enough '}'")

    return None


if __name__ == '__main__':
    initialize()

    tokens = ''
    pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
    for arg in sys.argv[1:]:
        try:
            tokens = tokenize(arg, pattern)
        except IOError:
            sys.exit('Error: Bad input file')

        evaluate(tokens)
        print('=' * _PRINT_WIDTH)
