#!/usr/bin/env python3

import inspect

global debugging
debugging = False
#debugging = True

def err(msg):
    print("Error: {0}(): {1}".format(inspect.stack()[1][3], msg))

def show(*s):
    """Print but only when debugging"""
    if debugging:
        print(*s)

def test_func(function, outputs, *inputs):
    """Test function with inputs and compare actual outputs with expected"""
    result = True

    for o, i in zip(outputs, *inputs):
        actual = function(*i)
        if(actual != o):
            result = False
            # Create visual seperation between failures
            debug('=' * _PRINT_WIDTH)
            debug(function.__name__ + "(" +  str(i).strip('[]()') + ")")
            debug('-' * _PRINT_WIDTH)
            debug("Actual:")
            debug(actual)
            debug('.' * _PRINT_WIDTH)
            debug("Expected:")
            debug(o)

    # Create visual seperation between tested functions, if there is need
    if(result == False):
        debug(('#' * _PRINT_WIDTH) + '\n')

    return result

def test_class(obj, outputs, *inputs):
    """Test object's class by applying inputs and comparing actual outputs with expected

    Takes an object, expected output, and a input set of the form (method, method_input)"""
    result = True

    # test_cass(stack, outputs, actions)
    # obj is of the class to be tested
    # apply set of actions on obj
    # check

    for output, input_list in zip(outputs, *inputs):

        for i in input_list:
            if hasattr(obj, *i[0]):
                method = getattr(obj, *i)
                actual = method(*i[1])
            else:
                print(type(obj).__name__ + " does not have the method " + method)
                #print(type(obj).__name__ + " does not have the method " + method.__name__)

        # Output of last input method is
        actual = function(*i)
        if(actual != output):
            result = False
            # Create visual seperation between failures
            debug('=' * _PRINT_WIDTH)
            debug(function.__name__ + "(" +  str(i).strip('[]()') + ")")
            debug('-' * _PRINT_WIDTH)
            debug("Actual:")
            debug(actual)
            debug('.' * _PRINT_WIDTH)
            debug("Expected:")
            debug(output)

    # Create visual seperation between tested functions, if there is need
    if(result == False):
        debug(('#' * _PRINT_WIDTH) + '\n')

    return result
