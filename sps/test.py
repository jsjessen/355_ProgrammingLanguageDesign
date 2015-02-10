#!/usr/bin/env python3

def debug(*s):
    """Print but only when debugging"""
    if debugging:
        print(*s)

def test(function, outputs, *inputs):
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
