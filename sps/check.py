#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

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


