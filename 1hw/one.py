#!/usr/bin/env python3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------


# Used this value because it's less than 80 and
# aligns nicely with both the histogram and digraph output.
_PRINT_WIDTH = 78

#debugging = True  # view debugging output
debugging = False  # hide debugging output


#================================= Test/Debug ==================================

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
            print('=' * _PRINT_WIDTH)
            # Display the function and its input
            print(function.__name__ + "(" +  str(i).strip('[]()') + ")")
            # Make actual and expected outputs easy to compare
            print('-' * _PRINT_WIDTH)
            print("Actual:")
            print(actual)
            print('.' * _PRINT_WIDTH)
            print("Expected:")
            print(o)

    if(result == False):
        # Create visual seperation between tested functions, if there is need
        print(('#' * _PRINT_WIDTH) + '\n')
    else:
        # So there is some indication if everything works
        print(function.__name__ + ": OK")

    return result


#================================ Translation ==================================

# Assumes that the characters in s1 are unique and
# that the two strings are the same length.
def makettable(s1, s2):
    """Return a dictionary mapping each char in s1 to corresponding char in s2"""
    ttable = {}

    for c1, c2 in zip(s1, s2):
        debug(c1, c2)
        ttable[c1] = c2

    return ttable


# The translation table is a dictionary.
# If a character is not in the translation table, it remains unchanged.
def trans(ttable, s):
    """Return Translation of string s using translation table ttable"""
    translation = ""

    for c in s:
        translation += ttable.get(c, c)

    return translation


def testtrans():
    """Test trans(), return false if there are any failures"""
    ttable = makettable('abc', 'xyz')
    revttable = makettable('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"

    inputs = []
    outputs = []

    inputs.append((ttable, tests))
    outputs.append(answer)

    inputs.append((revttable, trans(ttable, tests)))
    outputs.append("Now I know mb abc's")

    inputs.append((ttable, ''))
    outputs.append('')

    inputs.append((makettable('', ''), "abc"))
    outputs.append('abc')

    return test(trans, outputs, inputs)


#================================= Histogram ===================================

def histo(s):
    """Return a histogram depicting the frequency of each char in string s"""
    D = {}

    for c in s:
        D[c] = D.get(c, 0) + 1

    # Primary sort by frequency (High->Low)
    # Secondary sort alphabetically (A->Z)
    histogram = sorted(D.items(), key=lambda t: (-t[1], t[0]))

    return histogram


def testhisto():
    """Test histo(), return false if there are any failures"""
    inputs = []
    outputs = []

    inputs.append(('implemented',))
    outputs.append([('e', 3), ('m', 2), ('d', 1), ('i', 1), ('l', 1), ('n', 1),
                    ('p', 1), ('t', 1)])

    inputs.append(('abbccddd',))
    outputs.append([('d', 3), ('b', 2), ('c', 2), ('a', 1)])

    inputs.append(('aaabbccd',))
    outputs.append([('a', 3), ('b', 2), ('c', 2), ('d', 1)])

    return test(histo, outputs, inputs)


#================================== Digraphs ===================================

def digraphs(s):
    """Return digraphs depicting the frequency of adjacent characters in s"""
    D = {}

    for i in range(len(s) - 1):
        pair = '/' + s[i : i + 2] + '/'
        D[pair] = D.get(pair, 0) + 1

    # Primary sort alphabetically (A->Z)
    # Secondary sort by frequency (High->Low)
    digraph = sorted(D.items(), key=lambda t: (t[0], -t[1]))

    return digraph


def testdigraphs():
    """Test digraphs(), return false if there are any failures"""
    inputs = []
    outputs = []

    inputs.append(('abbccddddab',))
    outputs.append([('/ab/', 2), ('/bb/', 1), ('/bc/', 1), ('/cc/', 1),
                    ('/cd/', 1), ('/da/', 1), ('/dd/', 3)])

    inputs.append(('aaabbccd',))
    outputs.append([('/aa/', 2), ('/ab/', 1), ('/bb/', 1), ('/bc/', 1),
                    ('/cc/', 1), ('/cd/', 1)])

    inputs.append(('dccbbaaa',))
    outputs.append([('/aa/', 2), ('/ba/', 1), ('/bb/', 1), ('/cb/', 1),
                    ('/cc/', 1), ('/dc/', 1)])

    return test(digraphs, outputs, inputs)


#==================================== Main =====================================

if __name__ == '__main__':

    print()
    testtrans()
    testhisto()
    testdigraphs()
    print()


#================================ Extra Credit =================================

# ZYX WVWUTSZRVQ VP OUNMXLX WKZYVQL WNXLXQZTK XLZSOTRLYXJ RQ
# ZYX WSNI RL ZYX NXLUTZ VP SHHRJXQZST SQJ/VN RQZXQZRVQST NXTXSLXL OK
# WXZ VGQXNL. ZYXLX RQZNVJUHZRVQL HSQ YSFX JXFSLZSZRQE HVQLXDUXQHXL ZV
# VUN XHVLKLZXM. OUNMXLX WKZYVQL YSFX OXXQ PVUQJ ZV PXXJ VQ S GRJX
# FSNRXZK VP MSMMSTL SQJ ORNJL RQ ZYX XFXNETSJXL-XFXQ ZYX VHHSLRVQST
# STTRESZVN! OK WNXKRQE VQ QSZRFX GRTJTRPX, SQJ HVMWXZRQE GRZY VZYXN
# QSZRFX WNXJSZVNL, WKZYVQL SNX LXNRVULTK RMWSHZRQE ZYX QSZUNST VNJXN
# VP LVUZY PTVNRJS'L XHVTVERHST HVMMUQRZRXL. ZYX HVQZRQUXJ
# WNVTRPXNSZRVQ VP OUNMXLX WKZYVQL-SQJ ZYX HVQZRQUXJ RQZNVJUHZRVQ VP
# QXG PVNXREQ LWXHRXL-HSQ PUNZYXN ZYNXSZXQ MSQK VP ZYX XQJSQEXNXJ
# WTSQZL SQJ SQRMSTL GX'NX GVNIRQE JRTREXQZTK
# ZV WNVZXHZ. (GGG.QWL.EVF/XFXN/QSZUNXLHRXQHX/OUNMXLXWKZYVQLRQZNV.YZM)

# SOHJXPEYR*ITMQVWDNLZUFG*K*
# --------------------------
# abcdefghijklmnopqrstuvwxyz

thisIsTheCryptogramAnswer = """
the population of burmese pythons presently established in
the park is the result of accidental and/or intentional releases by
pet owners. these introductions can have devastating consequences to
our ecosystem. burmese pythons have been found to feed on a wide
variety of mammals and birds in the everglades-even the occasional
alligator! by preying on native wildlife, and competing with other
native predators, pythons are seriously impacting the natural order
of south florida's ecological communities. the continued
proliferation of burmese pythons-and the continued introduction of
new foreign species-can further threaten many of the endangered
plants and animals we're working diligently
to protect. (www.nps.gov/ever/naturescience/burmesepythonsintro.htm)
"""
