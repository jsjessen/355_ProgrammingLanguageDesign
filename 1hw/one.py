#!/usr/bin/env python3

# James Jessen
# 10918967
# CptS 355

# Developed for/on Linux, specifically Ubuntu 14.10 32-bit

#-------------------------------------------------------------------------------

import operator

#debugging = True
debugging = False

def debug(*s):
    """A clone of print(), toggleable with the boolean variable debugging"""
    if debugging: print(*s)


def test(i, o, expected):
    """Runs tests on a function given a list of inputs and expected outputs"""
    if (o == expected):
        return True
    else:
        print('=' * 78)
        print(i)
        print('-' * 78)
        print("Output:")
        print(o)
        print('.' * 78)
        print("Expected:")
        print(expected)
        return False


# The text of a message can be hidden by applying a translation function to each character. Define a function makettable(s1,s2) that returns a dictionary such that each character in s1 is mapped to the character at the corresponding position in s2. You may assume that the characters in s1 are unique and that the two strings are the same length. (When I say "you may assume X" it means that your code does not have to check whether X holds or not).
# So for example, makettable('abcdefg', 'gfedcba')
# returns {'a': 'g', 'c': 'e', 'b': 'f', 'e': 'c', 'd': 'd', 'g': 'a', 'f': 'b'}

def makettable(s1,s2):
    """Makes a translation table mapping string s1 to string s2"""
    debug('makettable: ' + '"'+s1+'"' + ' -> ' + '"'+s2+'"')
    ttable = {}
    for c1,c2 in zip(s1,s2):
        debug(c1,c2)
        ttable[c1] = c2
    return ttable


# Now, define a function trans(ttable, s). trans translates its string argument, s, according to its translation table argument, ttable. Argument ttable is, of course, a dictionary returned by themakettable function, and the result of trans is obtained by replacing each character, c, of s by ttable[c], if c is amongst the keys of the ttable. If however c is not in ttable.keys() then it is unchanged in the output. This is all harder to describe than to do! To easily look up k in dictionary, D, specifying that the same character is to be used if it is not present as a key in the dictionary you can use translation = D.get(k,k) # use help({}.get) to see more about get.

def trans(ttable, s):
    """Translates string s using translation table ttable"""
    debug('trans: ' + '"'+s+'"')
    translation = ""
    for c in s:
        translation += ttable.get(c,c)
    debug(translation)
    return translation


def testtrans():
    """Function to test translation code
       Returns True if successful, False if any test fails
    """
    ttable = makettable('abc', 'xyz')
    revttable = makettable('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"

    inputs = []
    outputs = []

    inputs.append([ttable, tests])
    outputs.append(answer)

    inputs.append([revttable, trans(ttable, tests)])
    outputs.append("Now I know mb abc's")

    inputs.append([ttable, ''])
    outputs.append('')

    inputs.append([makettable('',''), "abc"])
    outputs.append('abc')

    result = True
    for i,o in zip(inputs,outputs):
        if(test("trans(" + str(i).strip('[]') + ")", trans(i[0], i[1]), o) == False):
            result = False
    return result


# Define a function, histo(s) computing the histogram of a given string. (Look up histogram in the dictionary if you don't know what it means.) The histogram returned by the function is a list of characters in the input string s each paired with its frequency. Characters must appear in the list ordered from most frequent to least frequent. For example, histo('implemented') is [('e',3), ('m',2), ('d',1), ('i',1), ('l',1), ('n',1), ('p',1), ('t',1)]. (Characters with the same frequency must appear in increasing alphabetical order.) To implement the sorting you must use the python built-in function sorted.
# Do not write your own sorting code.
# Hint: help(sorted) and the Python documentation are your friends.

def histo(s):
    """Returns a histogram depicting the frequency of each char in string s"""
    debug('histo: ' + '"'+s+'"')
    D = {}
    for c in s:
        D[c] = D.get(c, 0) + 1
    # sorted by value then by key
    # check that sort is most to least frequent, then alphabetical
    histogram = sorted(D.items(), key=lambda t : (-t[1], t[0]))
    debug(histogram)
    return histogram


def testhisto():
    """Function to test histrogram code
       Returns True if successful, False if any test fails
    """

    inputs = []
    outputs = []

    inputs.append('implemented')
    outputs.append([('e',3), ('m',2), ('d',1), ('i',1), ('l',1), ('n',1),
                  ('p',1), ('t',1)])

    inputs.append('abbccddd')
    outputs.append([('d',3), ('b',2), ('c',2), ('a',1)])

    inputs.append('aaabbccd')
    outputs.append([('a',3), ('b',2), ('c',2), ('d',1)])

    result = True
    for i,o in zip(inputs,outputs):
        if(test('histo(' + '"'+i+'"' + ')', str(histo(i)), str(o)) == False):
            result = False
    return result


# A digraph is a pair of characters that occur adjacent to one another in a text. By convention we write each digraph between a pair of '/' characters to make it easier to see where the blanks are. For example the digraphs at the beginning of the first sentence of this section are /A /, / d/, /di/, /ig/, etc. Digraph frequency counts are helpful in cryptological analysis of some ciphers. Define a digraphs(s) function that returns a list containing the number of times each digraph occurs in string s. Digraphs must be listed in alphabetical order. Again, use the built-in function sorted and do not write your own sorting code. Digraphs that do not occur in the input (0 occurrences) should not be listed in the output.

# Here is what the function might return on some hypothetical sample input:
#
# [('/ </', 48), ('/ a/', 56), ('/ d/', 30), ('/ i/', 34), ('/ o/', 37),
# ('/ t/', 66), ('/. /', 31), ('/an/', 33), ('/co/', 47), ('/d /',38),
# ('/de/', 44), ('/e /', 83), ('/he/', 41), ('/in/', 53), ('/n /',40),
# ('/or/', 36), ('/r /', 32), ('/re/', 44), ('/s /', 44), ('/t /',36),
# ('/th/', 52), ('/to/', 42)

def digraphs(s):
    """Returns a digraph depicting the frequency of adjacent char in string s"""
    debug('digraphs: ' + '"'+s+'"')
    D = {}
    for i in range(len(s)-1):
        pair = '/' + s[i:i+2] + '/'
        D[pair] = D.get(pair, 0) + 1
    # sorted by key then by value
    digraph = sorted(D.items(), key=lambda t : (t[0], -t[1]))
    debug(digraph)
    return digraph


def testdigraphs():
    """Function to test digraph code
       Returns True if successful, False if any test fails
    """
    inputs = []
    outputs = []

# [('/ </', 48), ('/ a/', 56), ('/ d/', 30), ('/ i/', 34), ('/ o/',37),
#  ('/ t/', 66), ('/. /', 31), ('/an/', 33), ('/co/', 47), ('/d /',38),
#  ('/de/', 44), ('/e /', 83), ('/he/', 41), ('/in/', 53), ('/n /',40),
#  ('/or/', 36), ('/r /', 32), ('/re/', 44), ('/s /', 44), ('/t /',36),
#  ('/th/', 52), ('/to/', 42)

    inputs.append('abbccddddab')
    outputs.append([('/ab/', 2), ('/bb/', 1), ('/bc/', 1), ('/cc/', 1),
                    ('/cd/', 1), ('/da/', 1), ('/dd/', 3)])

    inputs.append('aaabbccd')
    outputs.append([('/aa/', 2), ('/ab/', 1), ('/bb/', 1), ('/bc/', 1),
                    ('/cc/', 1), ('/cd/', 1)])

    inputs.append('dccbbaaa')
    outputs.append([('/aa/', 2), ('/ba/', 1), ('/bb/', 1), ('/cb/', 1),
                    ('/cc/', 1), ('/dc/', 1)])

    for i,o in zip(inputs,outputs):
        test('digraphs(' + '"'+i+'"' + ')', str(digraphs(i)), str(o))

    result = True
    for i,o in zip(inputs,outputs):
        if(test('digraphs(' + '"'+i+'"' + ')', str(digraphs(i)), str(o)) == False):
            result = False
    return result


#===================================== Main ====================================
if __name__ == '__main__':

    if debug:
        passedMsg = "%s passed"
        failedMsg = "%s failed"

        print()
        if(testtrans()):    print("Translation...OK")
        if(testhisto()):    print("Histogram.....OK")
        if(testdigraphs()): print("Digraphs......OK")
        print()


#===============================================================================

# Use your trans, histo, and digraph functions in an interactive python session to try to figure out the following cryptogram. To make the functions available in the interactive session
#
# >>> from one import *
#
# If you haven't solved one of these before you may want to look on the web for hints on the relative frequencies of letters and digraphs in the English language. You can use your functions to try out different possibilities and get clues about the translation being used. (Digits and punctuation are not changed in this cryptogram.)
#
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
#
# Hint: use your makettable function to gradually build better and better translations between the uppercase cryptogram characters to lowercase plaintext characters to make it visually apparent which characters have been translated. Note numbers and punctuation in the cryptogram will appear unchanged in the answer.

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
