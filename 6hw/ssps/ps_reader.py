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
import check

class PostScriptReader:
    """Describe dict class"""
    def __init__(self):
        debug.show("Initializing reader...")
        self.scope = 'dynamic' # default scope mode
        self.opStack = ps_stack.PostScriptStack()
        self.dictStack = ps_dict.PostScriptDictStack()

    def __str__(self):
        return str(self.opStack) + str(self.dictStack)

    def _tokenize(self, fileName):
        """Given a file name, breaks down the text into meaningful tokens"""
        debug.show("Tokenizing...")
        try:
            f = open(fileName, 'r')
            code = f.read()
        except IOError:
            sys.exit('Error: Bad input file')
        f.close()
        pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
        return re.findall(pattern, code)

    def read(self, fileName):
        tokens = self._tokenize(fileName)
        self.evaluate(tokens)

    def readCodeBlock(self, tokens, p):
        """Read code between { } into an array of tokens and return new position"""
        codeBlock = []
        parenLevel = 1
        while p < len(tokens):
            t = tokens[p]
            p += 1
            if t == '}':
                parenLevel -= 1
                if parenLevel == 0:
                    break
                elif parenLevel < 0:
                    sys.exit("Error: Not enough '{' or too many '}'")
            elif t == '{':
                parenLevel += 1
            debug.show('    ' * parenLevel + "{}".format(t))
            codeBlock.append(t)

        if parenLevel > 0:
            sys.exit("Error: Too many '{' or not enough '}'")
        else:
            self.opStack.push(codeBlock)

        return p

    def evaluate(self, tokens):
        """Evaluate PostScript code"""
        debug.show("Evaluating: {}".format(tokens))
        if debug.debugging:
            input("Press enter to continue...")

        name = re.compile('/[a-zA-Z?].*')
        p = 0
        while p < len(tokens):
            t = tokens[p]
            p += 1

            debug.show(self)

            # { CODE BLOCK }
            if t == '{':
                p = self.readCodeBlock(tokens, p)

            # Print the operand and dictionary stacks
            elif t == 'stack':
                print(self)

            # LOGIC FLOW
            elif hasattr(self, '_' + t):
                getattr(self, '_' + t)()

            # STACK
            elif t == '=':
                print(self.opStack.pop())
            elif hasattr(self.opStack, t):
                getattr(self.opStack, t)()
            elif hasattr(self.opStack, t + '_'):
                getattr(self.opStack, t + '_')()

            # DICTIONARY
            elif t == 'def':
                value = self.opStack.pop()
                key = self.opStack.pop()
                if check.isString(key):
                    self.dictStack.define(key, value)
                else:
                    sys.exit("Error: '{}' has invalid operands".format(t))
            elif hasattr(self.dictStack, t):
                getattr(self.dictStack, t)()
            elif hasattr(self.dictStack, t + '_'):
                getattr(self.dictStack, t + '_')()

            elif name.match(t):
                self.opStack.push(t[1:])

            # Search for tok in dicts, starting with top dict and moving downward
            # if found, use key to get value, push value onto stack
            elif self.dictStack.defined(t):
                definition, link = self.dictStack.lookup(t)
                if check.isCode(definition):
                    self.dictStack.push({}, link, self.scope)
                    self.evaluate(definition) # call function
                    if self.scope == 'static':
                        self.dictStack.pop()      # return from function
                else:
                    self.opStack.push(definition)
            else:
                try:
                    # if it is a number push it
                    self.opStack.push(float(t))
                except:
                    sys.exit("Error: '{}' is not a valid token".format(t))
        return None


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
    def _if(self):
        """Execute code array if the condition is true"""
        debug.show("if:Stack = " + str(self.opStack))
        if self.opStack.size() >= 2:
            ifcode = self.opStack.pop()
            boolean = self.opStack.pop()
            if check.isCode(ifcode) and check.isBool(boolean):
                if check.boolValue(boolean):
                    debug.show("if:True")
                    evaluate(ifcode)
            else:
                debug.err("bad types on stack")
        else:
            debug.err("not enough items on the stack")
        debug.show("if:False")
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
    def _ifelse(self):
        """Execute first code array if the condition is true and the second if it is false"""
        debug.show("ifelse:Stack = " + str(self.opStack))
        if self.opStack.size() >= 3:
            falseCode = self.opStack.pop()
            trueCode = self.opStack.pop()
            boolean = self.opStack.pop()
            if check.isCode(falseCode) and check.isCode(trueCode) and check.isBool(boolean):
                if check.boolValue(boolean):
                    debug.show("ifelse:True")
                    self.evaluate(trueCode)
                else:
                    debug.show("ifelse:False")
                    self.evaluate(falseCode)
            else:
                debug.err("bad types on stack")
        else:
            debug.err("not enough items on the stack")
        return None
