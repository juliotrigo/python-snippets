# -*- coding: utf-8 -*-

"""module2 documentation

Created on 28 Jan 2013

@author: juliotrigo
"""

from . import module1

class _Class2(module1.Class1):
    
    """Class 2 documentation"""

    def __init__(self):
        """Constructor Class 2"""
        module1.Class1.__init__(self, 'John', 'Doe')