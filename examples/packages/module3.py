# -*- coding: utf-8 -*-

"""sibling module."""

#from __future__ import print_function, absolute_import, division, with_statement
#
#http://docs.python.org/2/library/__future__.html
#feature           optional   mandatory  effect
#
#nested_scopes     2.1.0b1    2.2        PEP 227: Statically Nested Scopes
#generators        2.2.0a1    2.3        PEP 255: Simple Generators
#division          2.2.0a2    3.0        PEP 238: Changing the Division Operator
#absolute_import   2.5.0a1    3.0        PEP 328: Imports: Multi-Line and Absolute/Relative
#with_statement    2.5.0a1    2.6        PEP 343: The “with” Statement
#print_function    2.6.0a2    3.0        PEP 3105: Make print a function
#unicode_literals  2.6.0a2    3.0        PEP 3112: Bytes literals in Python 3000

import sys

import examples.classes.module1


def module1_access():
    """Tests intra-package references."""
    c1 = examples.classes.module1.Class1()
    c1.method1()


def _not_public():
    """Tests _X and __all__"""
    print("Not public method.")


class MyClass(object):

    """My Class documentation."""

    def __init__(self, param):
        """MyClass constructor"""
        self.param = param

if __name__ == '__main__':
    print(list(sys.modules.keys()))
