#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import check
import ps_stack
import debug

class PostScriptDictStack(ps_stack.PostScriptStack):
    """PostScript Dictionary Stack"""
    def __init__(self):
        self.items = []
        self.push({})

    def __str__(self):
        """Display the contents of the dictionary stack, without modifying it"""
        myString =  '\n    Dictionary Stack   \n'
        myString += '***********************\n'
        for dic in reversed(self.items):
            for key in dic:
                myString += key + ': ' + str(dic[key]) + '\n'
            myString += '=======================\n'
        return myString

    def lookup(self, key):
        for dic in reversed(self.items):
            if key in dic:
                return dic[key]
        return None

    #   key value def (key = value)
    #
    #     |-------|
    #     | value |
    #     |-------|
    #     |  key  |
    #     |-------|
    #
    # The  def operator defines a name.  def requires its two operands to be on the stack:
    #    name (constant) to be defined and
    #    the value to which it will be bound
    def define(self, key, value):
        if check.isString(key):
            self.peek()[key] = value
        else:
            debug.err("Cannot use '{}' as key value".format(key))
        debug.show("Defined: {} = {}".format(key, value))
        return None

    # begin requires one dictionary operand on the operand stack
    def begin(self, newDict):
        """Create a new dictionary on the top of the dictionary stack"""
        self.push(newDict)
        return None
        if check.isDict(newDict):
            self.push(newDict)
        else:
            print(type(newDict).__name__)
            debug.err("Attempting to add non-dict to dictionary stack")
        return None

    def end(self):
        """Remove the a dictionary from the top of the dictionary stack"""
        self.pop()
        return None
