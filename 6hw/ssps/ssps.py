#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

# Scoped Simple PostScript (SSPS)
#-------------------------------------------------------------------------------

import sys
import ps_reader
import disp

global SCOPE_MODE
SCOPE_MODE = 'dynamic' #set defualt

# python3 ssps.py A -s B -d C
# A executed using dynamic scope rules
# B executed using static scope rules
# C executed using dynamic scope rules

if __name__ == '__main__':
    reader = ps_reader.PostScriptReader()

    # Read each file with the assumption that it contains PostScript code
    for arg in sys.argv[1:]:
        if arg == '-d':
            SCOPE_MODE = 'dynamic'
        elif arg == '-s':
            SCOPE_MODE = 'static'
        else:
            reader.read(arg)
            print(reader)
            print('#' * disp.WIDTH_BIG + '\n')
