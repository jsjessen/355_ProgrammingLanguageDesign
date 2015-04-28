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
import disp

class PostScriptDictStack(ps_stack.PostScriptStack):
    """PostScript Dictionary Stack"""
    def __init__(self):
        self.items = []
        self.push({}, -1, 'static')

    def __str__(self):
        """Represent the dictionary stack as a string"""
        #width = disp.WIDTH_MED
        #myString = disp.center_title('Dictionary Stack', width)
        myString = '=' * disp.WIDTH_SMALL + '\n'
        length = self.size() - 1
        for i, (dic, static_link) in enumerate(reversed(self.items)):
            index = length - i
            if static_link < 0:
                static_link = 0
            myString += '---- ' + str(index)
            myString += ' ---- ' + str(static_link) + ' ----\n'
            for key, value in dic.items():
                myString += key + ': '
                if check.isCode(value):
                    myString += '[ '
                    for code in value:
                        myString += code + ' '
                    myString += ']\n'
                else:
                    myString += str(value) + '\n'
        myString += '=' * disp.WIDTH_SMALL + '\n'
        return myString

    def size(self):
        """Determine the number of dictionaries in the stack"""
        return len(self.items)

    # At the point when a function is called the static link in the new stack entry
    # needs to be set to point to the stack entry where the function’s definition was found.
    # (Note that with the stack being a list, this “pointer” is just an index in the list.)
    def push(self, dic, link, scope):
        """Add a new dictionary to the top of the stack"""
        if check.isDict(dic) and check.isNum(link):
            if scope == 'dynamic':
                self.items.append((dic, self.size() - 1)) # just use index
            elif scope == 'static':
                self.items.append((dic, link))
            else:
                debug.err('unknown scope mode')
        else:
            debug.err('Attempting to push bad types to Dictionary Stack')
        return None

    def pop(self):
        """Pop the first item off the stack and return it"""
        if self.size() <= 1:
            debug.err("dictionary stack is empty")
            return None
        else:                   # The stack has at least one item
            debug.show('dictStack.pop()')
            return self.items.pop()  # Return the last item of the stack

    def peek(self):
        """Read the top item off the stack without removing it"""
        debug.show('dictStack.peek()')
        return self.items[-1]

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
        """Add variable or function to the current dictionary"""
        if check.isString(key):
            dic, link = self.peek()
            dic[key] = value
        else:
            debug.err("Cannot use '{}' as key value".format(key))
        debug.show("Defined: {} = {}".format(key, value))
        return None

    # As discussed in class, variable lookups using static scope rules proceed by
    # looking in the current dictionary at the top of the dictionary stack
    # and then following the static-link fields to other dictionaries.
    def lookup(self, key):
        """Look up the value of a variable or function in the dictionary stack

        Start at the top dictionary on the stack and follow the link
        Assume the link was made to be dynamic/static when created
        """
        bottom_dic, bottom_link = self.items[0]
        link_to_me = self.size() - 1
        dic, link_to_parent = self.peek()
        while link_to_me >= 0:
            if key in dic:
                return dic[key], link_to_me
            link_to_me = link_to_parent
            dic, link_to_parent = self.items[link_to_parent]
        return None

    def defined(self, key):
        for dic, link in self.items:
            if key in dic:
                return True
        return False
