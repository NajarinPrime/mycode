#!/usr/bin/env python3
""" Author: Manuel Figueroa | Learning about Functions"""

import crayons

def slappy():
    """ This is to print strings in red """
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

def snork():
    """ This is to print in red and bold """
    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

def nombre():
    """ Prints my name in my favorite color """
    print(crayons.blue('Manuel', bold=True))

def main():
    """ These are functions that main can call """
    snork()
    slappy()
    nombre()
if __name__ == "__main__":
    main()
