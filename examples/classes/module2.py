# -*- coding: utf-8 -*-

"""module2 documentation"""

from . import module1

class _Class2(module1.Class1):
    
    """Class 2 documentation"""

    def __init__(self):
        """Constructor Class 2"""
        module1.Class1.__init__(self, 'John', 'Doe')