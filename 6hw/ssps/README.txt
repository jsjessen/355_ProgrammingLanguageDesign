James Jessen
10918967
CptS 355

Homework #6
Scoped Simple PostScript (SSPS)

-----------
Environment
-----------
Linux/Unix
Python 3.2.3

-------
Example
-------
python3 ssps.py fileA -s fileB -d fileC -s fileD fileE

    Result:
        fileA interpreted using dynamic scope rules
        fileB interpreted using static scope rules
        fileC interpreted using dynamic scope rules
        fileD interpreted using static scope rules
        fileE interpreted using static scope rules
