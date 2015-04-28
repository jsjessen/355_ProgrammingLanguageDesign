#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#================================= Checks ======================================

import debug

def isNum(item):
    """Check if the item is a number"""
    if isinstance(item, float) or isinstance(item, int):
        return True
    else:
        debug.show("{0} is a {1} not a number.".format(item, type(item).__name__))
        return False

def isDict(item):
    """Check if the item is a dictionary"""
    if isinstance(item, dict):
        return True
    else:
        debug.show("{0} is a {1} not a dictionary.".format(item, type(item).__name__))
        return False

def isList(item):
    """Check if the item is a list"""
    if isinstance(item, list):
        return True
    else:
        #debug.show("{0} is a {1} not a list.".format(item, type(item).__name__))
        return False

isCode = isList

def isString(item):
    """Check if the item is a string"""
    if isinstance(item, str):
        return True
    else:
        debug.show("{0} is a {1} not a string.".format(item, type(item).__name__))
        return False

def isBool(item):
    """Check if the item is a boolean"""
    if item in ('true', 'false'):
        return True
    else:
        debug.show("{0} is a {1} not a boolean.".format(item, type(item).__name__))
        return False

def boolValue(item):
    """Check the value of a boolean"""
    if item == 'true':
        return True
    elif item == 'false':
        return False
    else:
        return None
