#!/usr/bin/env python3
# Python 3.2.3
# Linux/Unix

# James Jessen
# 10918967
# CptS 355

#-------------------------------------------------------------------------------

import sys
import ps_reader

if __name__ == '__main__':
    reader = ps_reader.PostScriptReader()
    # Read each file with the assumption that it contains PostScript code
    for arg in sys.argv[1:]:
        reader.read(arg)
        print(reader)
        print('=' * 80)
