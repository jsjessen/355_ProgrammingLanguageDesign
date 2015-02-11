#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

import debug
#============================= Stack Operators =================================

class Stack:
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
        if not self.items:           # If the stack is empty
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
        self.items.push(stack[-1])
        return None

    def exch(self):
        """Exchange the top two stack values"""
        debug.show('stack.exch()')
        first, second = pop(), pop()
        push(first)
        push(second)
        return None

    def stack(self):
        """showlay the contents of the stack, without modifying it"""
        for item in reversed(self.items):
            print(item)
        print('=======================')
        return None

    # Call this function when you encounter '='
    def peek(self):
        debug.show('stack.peek()')
        """Pop the top item off of the stack and print it"""
        print(self.items.pop())
        return None

