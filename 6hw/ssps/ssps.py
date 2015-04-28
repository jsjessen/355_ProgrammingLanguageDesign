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

# python3 ssps.py A -s B -d C
# A executed using dynamic scope rules
# B executed using static scope rules
# C executed using dynamic scope rules

if __name__ == '__main__':
    reader = ps_reader.PostScriptReader()
    scope = 'dynamic'

    # Read each file with the assumption that it contains PostScript code
    for arg in sys.argv[1:]:
        if arg == '-d':
            scope = 'dynamic'
        elif arg == '-s':
            scope = 'static'
        else:
            width = disp.WIDTH_MED
            print('\n' + disp.center_title(arg + ' ('+ scope + ')', width, '#'))
            reader.scope = scope
            reader.read(arg)
            reader = ps_reader.PostScriptReader()
