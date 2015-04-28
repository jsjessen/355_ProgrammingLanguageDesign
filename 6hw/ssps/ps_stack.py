#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import debug
import check
import disp

class PostScriptStack:
    """PostScript Stack"""
    def __init__(self):
        self.items = []

    def __str__(self):
        """Represent the stack as a string"""
        # width = disp.WIDTH_MED
        # myString = disp.center_title('Operand Stack', width)
        myString = '=' * disp.WIDTH_SMALL + '\n'
        for item in reversed(self.items):
            myString += str(item) + '\n'
        return myString

    def stack(self):
        """Show the contents of the stack, without modifying it"""
        print(self)

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
            print('Error: The stack is empty')
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

    # Call this function when you encounter '='
    def peek(self):
        """Read the top item off the stack without removing it"""
        debug.show('stack.peek()')
        return self.items[-1]

    #(Normally Postscript uses a dict operator requiring one operand. Our SPS has the dictz operator with zero operands. You can run regular postscript code in your interpreter if you prefix the Postscript code by /dict {pop dictz} def, to provide a sensible definition for the missing dict operation.)
    #def dictz(self):
    #    """Push an empty dictionary on to the operand stack"""
    #    self.push({})
    #    return None

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
            second, first = self.pop(), self.pop()
            if check.isNum(first) and check.isNum(second):
                self.push(first + second)
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
            if check.isNum(first) and check.isNum(second):
                self.push(first - second)
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
            second, first = self.pop(), self.pop()
            if check.isNum(first) and check.isNum(second):
                self.push(first * second)
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
            if check.isNum(first) and check.isNum(second):
                self.push(first / second)
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
            if check.isNum(first) and check.isNum(second):
                self.push(first // second)
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
            num = self.pop()
            if check.isNum(num):
                self.push(-num)


#============================ Comparison Operators =============================

    def eq(self):
        """Equal to"""
        if self.size() >= 2:
            if self.pop() == self.pop():
                self.push('true')
            else:
                self.push('false')
        return None

    def lt(self):
        """Less than"""
        if self.size() >= 2:
            if self.pop() > self.pop():  # (2 4 lt) = (2 < 4) = (4 > 2)
                self.push('true')
            else:
                self.push('false')
        return None

    def gt(self):
        """Greater than"""
        if self.size() >= 2:
            if self.pop() < self.pop():  # (4 2 gt) = (4 > 2) = (2 < 4)
                self.push('true')
            else:
                self.push('false')
        return None


#============================== Boolean Operators ==============================

    def and_(self):
        """ ? """
        if self.size() >= 2:
            if check.boolValue(self.pop()) and check.boolValue(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None

    def or_(self):
        """ ? """
        if self.size() >= 2:
            if check.boolValue(self.pop()) or check.boolValue(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None

    def not_(self):
        """ ? """
        if self.size() >= 2:
            if not check.boolValue(self.pop()):
                self.push('true')
            else:
                self.push('false')
        return None


#================================== Testing ====================================

#def test():
#    """Test functionality of the PostScriptStack class"""
#    print("Testing Stack")
#    print("=============")
#    if(test_basic()):
#        print("Basic Stack Operations...OK")
#    if(test_math()):
#        print("Mathematical Operations...OK")
#    if(test_comp()):
#        print("Comparison Operations...OK")
#    if(test_bool()):
#        print("Boolean Operations...OK")
#
#    return None
#
#def test_basic():
#    """Test basic stack functions"""
#    stack = PostScriptStack()
#    inputs = []
#    outputs = []
#
#    # isEmpty(self):
#    # push(self, item):
#    # pop(self):
#    # size(self):
#    # clear(self):
#    # dup(self):
#    # exch(self):
#    # disp(self):
#    # peek(self):
#
#    return debug.test_class(stack, inputs, outputs)
#
#def test_math():
#    """Test mathematical operation functions"""
#    stack = PostScriptStack()
#    inputs = []
#    outputs = []
#
## add(self):
#
## sub(self):
#    # 8 - 5 = 3
#    inputs.append((stack.push(8), stack.push(5), stack.sub()))
#    outputs.append(1)
#    # 2 - 12 = -10
#    inputs.append((stack.push(2), stack.push(12), stack.sub()))
#    outputs.append(1)
#    # -4 - -6 = 2
#    inputs.append((stack.push(-4), stack.push(-6), stack.sub()))
#    outputs.append(1)
#
## mul(self):
#
## div(self):
#
## idiv(self):
#
## neg(self):
#
#    return debug.test_class(stack, inputs, outputs)
#
#def test_comp(stack):
#    """Test comparison operation functions"""
#    stack = PostScriptStack()
#    inputs = []
#    outputs = []
#
#    # eq(self):
#    # lt(self):
#    # gt(self):
#
#    return debug.test_class(stack, inputs, outputs)
#
#def test_bool(stack):
#    """Test boolean operation functions"""
#    stack = PostScriptStack()
#    inputs = []
#    outputs = []
#
#    # and_(self):
#    # or_(self):
#    # not_(self):
#
#    return debug.test_class(stack, inputs, outputs)
