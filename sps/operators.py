
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
#     |...|     |...|
#     |___|     |___|
def add():
    """Addition"""
    if len() >= 2: # stack has at least 2 items
        push(isNum(pop()) + isNum(pop()))
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
#     |...|     |...|
#     |___|     |___|
def sub():
    """Subtraction"""
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) - isNum(pop()))
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
#     |...|     |...|
#     |___|     |___|
def mul():
    """Multiplication"""
    if len() >= 2: # stack has at least 2 items
        push(isNum(pop()) * isNum(pop()))
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
#     |...|     |...|
#     |___|     |___|
def div():
    """ Divide the second number on the stack by the top number on the stack """
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) / isNum(pop()))
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
#     | ... |     |...|
#     |_____|     |___|
def idiv():
    """Divide the second number on the stack by the top number on the stack"""
    if len() >= 2: # stack has at least 2 items
        exch()
        push(isNum(pop()) // isNum(pop()))
    return None

# (2 neg) = (-2) = -2
#
#     |---|
#     |neg|
#     |---|     |----|
#     | 2 |     | -2 |
#     |---| ==> |----|
#     |...|     |....|
#     |___|     |____|
def neg():
    """Negate the top number on the stack"""
    if len() >= 1:
        push(-isNum(pop()))


#============================ Comparison Operators =============================

def eq():
    """Equal to"""
    if len() >= 2:
        if isNum(pop()) == isNum(pop()):
            push('true')
        else:
            push('false')
    return None

def lt():
    """Less than"""
    if len() >= 2:
        if isNum(pop()) > isNum(pop()): # (2 4 lt) = (2 < 4) = (4 > 2)
            push('true')
        else:
            push('false')
    return None

def gt():
    """Greater than"""
    if len() >= 2:
        if isNum(pop()) < isNum(pop()): # (4 2 gt) = (4 > 2) = (2 < 4)
            push('true')
        else:
            push('false')
    return None


#============================== Boolean Operators ==============================

def and_():
    """ ? """
    if len() >= 2:
        if isBool(pop()) and isBool(pop()):
            push('true')
        else:
            push('false')
    return None

def or_():
    """ ? """
    if len() >= 2:
        if isBool(pop()) or isBool(pop()):
            push('true')
        else:
            push('false')
    return None

def not_():
    """ ? """
    if len() >= 2:
        if not isBool(pop()):
            push('true')
        else:
            push('false')
    return None


#============================ Sequencing Operators =============================

def if_():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evaluate(ifcode)
    return None

# NOT IMPLEMENTED !!!
def if_else():
    """ ? """
    ifcode = isCode(pop()) # Make sure it is code (a list)
    if chBool(pop()):
        evalLoop(ifcode)
    return None
