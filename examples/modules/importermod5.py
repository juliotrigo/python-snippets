# -*- coding: utf-8 -*-

"""Imports attributes from other modules.

Created on 17 Feb 2013

@author: juliotrigo

This module cannot be executed as a script (__name__ = __main__):
ValueError: Attempted relative import in non-package

http://www.python.org/dev/peps/pep-0328/
PEP 328 -- Imports: Multi-Line and Absolute/Relative

Relative Imports and __name__

Relative imports use a module's __name__ attribute to determine that module's 
position in the package hierarchy. 
If the module's name does not contain any package information 
(e.g. it is set to '__main__') then relative imports are resolved as 
if the module were a top level module, regardless of where the module is actually 
located on the file system.
"""

from .module6 import y, printer6
from . import module5

def actions():
    y = "New value for y."          # It does not change the y value in module6
    module5.x = "New value for x."

    printer6()
    module5.printer5()