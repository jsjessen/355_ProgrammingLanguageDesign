# James Jessen
# 10918967
# CptS 355
# Intended for Linux

import operator

debugging = True

def debug(*s): if debugging: print(*s)

#debug("This is debug output")


# The text of a message can be hidden by applying a translation function to each character.
# Define a function makettable(s1,s2) that returns a dictionary such that each character in s1 is
# mapped to the character at the corresponding position in s2. You may assume that the characters in
# s1 are unique and that the two strings are the same length. (When I say "you may assume X" it means
# that your code does not have to check whether X holds or not). So for example,
# makettable('abcdefg', 'gfedcba') returns {'a': 'g', 'c': 'e', 'b': 'f', 'e':
# 'c', 'd': 'd', 'g': 'a', 'f': 'b'}

def makettable(s1,s2):
    """Makes a table mapping string s1 to string s2"""
    table = {}
    for c1,c2 in s1,s2
       table[c1] = c2
    return table


# Now, define a function trans(ttable, s). trans translates its string argument, s, according to its
# translation table argument, ttable. Argument ttable is, of course, a dictionary returned by the
# makettable function, and the result of trans is obtained by replacing each character, c, of s by
# ttable[c], if c is amongst the keys of the ttable. If however c is not in ttable.keys() then it is
# unchanged in the output. This is all harder to describe than to do! To easily look up k in dictionary, D,
# specifying that the same character is to be used if it is not present as a key in the dictionary you can use
# translation = D.get(k,k) # use help({}.get) to see more about get

def trans(ttable, s):
    """Translates string s using the translation table"""
    for c in s:
        translation += ttable.get(c,c)
    return translation


def testtrans():
    """Function to test translation code

    Returns True if successful, False if any test fails
    """

    ttable = makettable('abc', 'xyz')
    revttable = makettable('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"

    if trans(ttable, tests) != answer: return False
    if trans(revttable, trans(ttable, tests)) != "Now I know mb abc's": return False
    if trans(ttable,'') != '': return False
    if trans(makettable('',''), "abc") != 'abc': return False
    return True

# Define a function, histo(s) computing the histogram of a given string. (Look up histogram in the
# dictionary if you don't know what it means.) The histogram returned by the function is a list of
# characters in the input string s each paired with its frequency. Characters must appear in the list ordered
# from most frequent to least frequent. For example, histo('implemented') is [('e',3),
# ('m',2), ('d',1),('i',1), ('l',1), ('n',1), ('p',1), ('t',1)]. (Characters
# with the same frequency must appear in increasing alphabetical order.) To implement the sorting you
# must use the python built-in function sorted. Do not write your own sorting code. (Hint:
# help(sorted) and the Python documentation are your friends.)

def histo(s):
    """Given a string, returns a histogram"""
    D = {}
    for c in s:
        D[c] += 1
    return sorted(D.items(), key=operator.itemgetter(1,0)) # sort by value then by key


def testhisto():
    """Function to test histrogram code

    Returns True if successful, False if any test fails
    """

# A digraph is a pair of characters that occur adjacent to one another in a text. By convention we write
# each digraph between a pair of '/' characters to make it easier to see where the blanks are. For
# example the digraphs at the beginning of the first sentence of this section are /A /, / d/, /di/,
# /ig/, etc. Digraph frequency counts are helpful in cryptological analysis of some ciphers.
# Define a digraphs(s) function that returns a list containing the number of times each digraph occurs
# in string s. Digraphs must be listed in alphabetical order. Again, use the built-in function sorted and do
# not write your own sorting code. Digraphs that do not occur in the input (0 occurrences) should not be
# listed in the output.

def digraphs(s):
    """Given a string, returns a digraph"""
    D = {}
    for i in range(len(s)-2):
        D[s[i:i+2]] += 1
    return sorted(D.items(), key=operator.itemgetter(0,1)) # sort by key then by value

# Here is what the function might return on some hypothetical sample input:
#
# [('/ </', 48), ('/ a/', 56), ('/ d/', 30), ('/ i/', 34), ('/ o/', 37),
# ('/ t/', 66), ('/. /', 31), ('/an/', 33), ('/co/', 47), ('/d /',38),
# ('/de/', 44), ('/e /', 83), ('/he/', 41), ('/in/', 53), ('/n /',40),
# ('/or/', 36), ('/r /', 32), ('/re/', 44), ('/s /', 44), ('/t /',36),
# ('/th/', 52), ('/to/', 42)

def testdigraphs():
    """Function to test digraph code

    Returns True if successful, False if any test fails
    """
    print("testdigraph: not yet implemented")


if __name__ == '__main__':

    passedMsg = "%s passed"
    failedMsg = "%s failed"

    if testttrans():
        print ( passedMsg % 'testtrans' )
    else:
        print ( failedMsg % 'testtrans' )

# etc. for the other tests.
# notice how you are repeating a lot of code here
# think about how you could avoid that -- we will discuss in class


#==============================================================================

# Use your trans, histo, and digraph functions in an interactive python session to try to figure out
# the following cryptogram. To make the functions available in the interactive session
#
# >>> from one import *
#
# If you haven't solved one of these before you may want to look on the web for hints on the relative
# frequencies of letters and digraphs in the English language. You can use your functions to try out
# different possibilities and get clues about the translation being used. (Digits and punctuation are not
# changed in this cryptogram.)
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
# Hint: use your makettable function to gradually build better and better translations between the
# uppercase cryptogram characters to lowercase plaintext characters to make it visually apparent which
# characters have been translated. Note numbers and punctuation in the cryptogram will appear
# unchanged in the answer.

thisIsTheCryptogramAnswer = """

answer

"""
