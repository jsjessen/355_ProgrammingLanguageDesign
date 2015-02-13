#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import debug
import check

class PostScriptStack:
    """Describe stack class"""
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        """Push an item onto the stack"""
        debug.show('stack.push({})'.format(item))
        self.items.append(item)      # append new item to the end of list
        return None

    def pop(self):
        """Pop the first item off the stack and return it"""
        if self.isEmpty():
            debug.err("stack is empty")
            return None
        else:                   # The stack has at least one item
            debug.show('stack.pop()')
            return self.items.pop()  # Return the last item of the stack

    # Call this function when you encounter "len"
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

    def clear(self):
        """Empty the stack"""
        debug.show('stack.clear()')
        self.items[:] = []
        return None

    def dup(self):
        """Duplicate the top item of the stack"""
        debug.show('stack.dup()')
        self.push(self.peek())
        return None

    # 9 4 exch:
    #
    #         |---|                         |---|
    #   first | 4 |                         | 9 | second
    #         |---|               |---|     |---|
    #  second | 9 |               | 4 |     | 4 | first
    #         |---| ==> |---| ==> |---| ==> |---|
    def exch(self):
        """Exchange the top two stack values"""
        debug.show('stack.exch()')
        first, second = self.pop(), self.pop()
        self.push(first)
        self.push(second)
        return None

    def disp(self):
        """show the contents of the stack, without modifying it"""
        for item in reversed(self.items):
            print(item)
        print('=======================')
        return None
    stack = disp
    # def stack(self):
    #     self.disp()
    #     return None

    # Call this function when you encounter '='
    def peek(self):
        """Pop the top item off of the stack and print it"""
        debug.show('stack.peek()')
        return self.items[-1]

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
    def add(self):
        """Addition"""
        debug.show('add()')
        if self.size() >= 2: # stack has at least 2 items
            self.push(check.isNum(self.pop()) + check.isNum(self.pop()))
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
    def sub(self):
        """Subtraction"""
        if self.size() >= 2: # stack has at least 2 items
            second, first = self.pop(), self.pop()
            self.push(check.isNum(first) - check.isNum(second))
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
    def mul(self):
        """Multiplication"""
        if self.size() >= 2: # stack has at least 2 items
            self.push(check.isNum(self.pop()) * check.isNum(self.pop()))
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
    def div(self):
        """ Divide the second number on the stack by the top number on the stack """
        if self.size() >= 2: # stack has at least 2 items
            second, first = self.pop(), self.pop()
            self.push(check.isNum(first) / check.isNum(second))
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
    def idiv(self):
        """Divide the second number on the stack by the top number on the stack"""
        if self.size() >= 2: # stack has at least 2 items
            second, first = self.pop(), self.pop()
            self.push(check.isNum(first) // check.isNum(second))
        return None

    # (2 neg) = (-2) = -2
    #
    #     |---|
    #     |neg|
    #     |---|     |----|
    #     | 2 |     | -2 |
    #     |---| ==> |----|
    def neg(self):
        """Negate the top number on the stack"""
        if self.size() >= 1:
            self.push(-check.isNum(self.pop()))


    #============================ Comparison Operators =============================

    def eq(self):
        """Equal to"""
        if self.size() >= 2:
            if check.isNum(self.pop()) == check.isNum(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None

    def lt(self):
        """Less than"""
        if self.size() >= 2:
            if check.isNum(self.pop()) > check.isNum(self.pop()): # (2 4 lt) = (2 < 4) = (4 > 2)
                self.push('true')
            else:
                self.push('false')
        return None

    def gt(self):
        """Greater than"""
        if self.size() >= 2:
            if check.isNum(self.pop()) < check.isNum(self.pop()): # (4 2 gt) = (4 > 2) = (2 < 4)
                self.push('true')
            else:
                self.push('false')
        return None

    #============================== Boolean Operators ==============================

    def and_(self):
        """ ? """
        if self.size() >= 2:
            if check.isBool(self.pop()) and check.isBool(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None

    def or_(self):
        """ ? """
        if self.size() >= 2:
            if check.isBool(self.pop()) or check.isBool(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None

    def not_(self):
        """ ? """
        if self.size() >= 2:
            if not check.isBool(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None
