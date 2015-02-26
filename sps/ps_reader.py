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

    def evaluate(self, tokens):
        """Evaluate PostScript code"""
        debug.show("Evaluating: {}".format(tokens))
        if debug.debugging:
            input("Press enter to continue...")

        # NUMBER
        try:
            self.opStack.push(float(tokens))
            return None
        except TypeError:
            pass
        except ValueError:
            pass
        # STRING LITERAL
        if check.isString(tokens) and tokens[0] == '/':
            self.opStack.push(tokens[1:])
            return None

        parenLevel = 0
        codeBlock = []
        for t in tokens:

            # { }
            if t == '}':
                parenLevel -= 1
                if(parenLevel == 0):
                    self.opStack.push(codeBlock)
                    codeBlock = []
                    continue
                elif(parenLevel < 0):
                    sys.exit("Error: Not enough '{' or too many '}'")
            debug.show('    ' * parenLevel + "{}".format(t))
            if t == '{':
                if parenLevel > 0:
                    codeBlock.append(t)
                parenLevel += 1
                continue

            if parenLevel > 0:
                codeBlock.append(t)
                continue

            # =
            if t == '=':
                print(self.opStack.pop())
                continue

            # NUMBER
            try:
                self.opStack.push(float(t))
                continue
            except ValueError:
                pass

            # STRING LITERAL
            if check.isString(t) and t[0] == '/':
                self.opStack.push(t[1:])
                continue

            # LOGIC FLOW
            if hasattr(self, '_' + t):
                getattr(self, '_' + t)()
                continue

            # STACK
            if hasattr(self.opStack, t):
                getattr(self.opStack, t)()
                continue
            if hasattr(self.opStack, t + '_'):
                getattr(self.opStack, t + '_')()
                continue

            # DICTIONARY
            if t == 'def':
                value = self.opStack.pop()
                key = self.opStack.pop()
                self.dictStack.define(key, value)
                continue
            if t == 'begin':
                debug.show("Top of stack: {}".format(self.opStack.peek()))
                self.dictStack.begin(self.opStack.pop())
                continue
            if hasattr(self.dictStack, t):
                getattr(self.dictStack, t)()
                continue
            if hasattr(self.dictStack, t + '_'):
                getattr(self.dictStack, t + '_')()
                continue

            # search for tok in dicts, starting with top dict and moving downward
            # if found, use key to get value, push value onto stack
            newTokens = self.dictStack.lookup(t)
            if newTokens is not None:
                self.evaluate(newTokens)
            else:
                sys.exit("Error: '{}' is undefined".format(t))

        if parenLevel > 0:
            sys.exit("Error: too many '{' or not enough '}'")

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
            ifcode = isCode(self.opStack.pop()) # Make sure it is code (a list)
            if check.isBool(self.opStack.pop()):
                debug.show("if:True")
                evaluate(ifcode)
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
            falseCode = check.isCode(self.opStack.pop()) # Make sure it is code (a list)
            trueCode = check.isCode(self.opStack.pop()) # Make sure it is code (a list)
            if check.isBool(self.opStack.pop()):
                debug.show("ifelse:True")
                self.evaluate(trueCode)
            else:
                debug.show("ifelse:False")
                self.evaluate(falseCode)
        else:
            debug.err("not enough items on the stack")
        return None
