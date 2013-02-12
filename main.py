# -*- coding: utf-8 -*-

"""Top level script.

Created on 9 Feb 2013

@author: juliotrigo
"""

import examples.classes.module2

from examples.packages import *

if __name__ == '__main__':   
    c2 = examples.classes.module2._Class2()
    
    module3.module1_access()
    #module4._not_public()  # module4 in not listed in examples.packages__init__.__all__
    
    