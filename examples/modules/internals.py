# -*- coding: utf-8 -*-

"""Exposing module internals.

__builtins__
__file__
__package__
__cached__
__name__
__doc__
"""

import sys

from . import module5

def actions():
    print(module5.__dict__.keys())
    #print(module5.__builtins__)
    print(module5.__file__)
    print(module5.__package__)
    print(module5.__cached__)
    print(module5.__name__)
    #print(module5.__doc__)

    print(module5.__dict__['x'])                        # Index namespace dictionary
    print(sys.modules['examples.modules.module5'].x)    # Index loaded-modules table
    print(getattr(module5, 'x'))                        # Call built-in fetch function