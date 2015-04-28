#!/usr/bin/env python3

global WIDTH_BIG
global WIDTH_MED
global WIDTH_SMALL

WIDTH_BIG = 80
WIDTH_MED = 60
WIDTH_SMALL = 20

def center_title(title, width):
    """Given a title and width, centers the title with spaces on either side"""
    title = ' ' + title + ' '
    spacing = (width - len(title)) // 2
    title =  '\n' + '=' * spacing + title + '=' * spacing + '\n'
    return title
