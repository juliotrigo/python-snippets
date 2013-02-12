# -*- coding: utf-8 -*-

"""Classes  top-level script.

Created on 28 Jan 2013

@author: juliotrigo
"""

from . import module1 
from . import module2


if __name__ == '__main__':
    print('object doc: ' + object.__doc__)
    
    print('module1 name: ' + module1.__name__)
    print('module1 doc: ' + module1.__doc__)
    print(module1.__dict__.keys())
    
    # MODULE 2
    c2 = module2._Class2()
    print('C2 name: ' + module2._Class2.__name__)
    print('C2 doc: ' + module2._Class2.__doc__)
    print(dir(module2._Class2))
    
    c2.method1()
    c2._Class1__method3()