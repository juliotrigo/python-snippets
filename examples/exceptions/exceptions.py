# -*- coding: utf-8 -*-

"""Exceptions.

Created on 24 Feb 2013

@author: juliotrigo
"""

class MyException(Exception):
    
    """General base exception."""
    
    def __init__(self, value):
        """Assigns the text error."""
        self.value = value
        
    def __str__(self):
        """Prints the error."""
        return str(self.value)
    
class IncorrectParameters(MyException):
    """The parameters are incorrect."""