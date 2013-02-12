# -*- coding: utf-8 -*-

"""General statements.

Created on 9 Feb 2013

@author: juliotrigo
"""

import sys

import examples.packages.module3

if __name__ == '__main__':
    print("***** sys.path *****")
    print(type(sys.path))
    print(sys.path)
    print("********************")
    
    examples.packages.module3.module1_access()