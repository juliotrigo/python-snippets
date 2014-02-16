#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Top level script."""

import examples.classes.module2
from examples.classes import *      # pylint: disable=W0401
from examples.packages import *     # pylint: disable=W0401

if __name__ == '__main__':
    c2 = examples.classes.module2._Class2()

    module3.module1_access()
    #module4._not_public()    # module4 in not listed in examples.packages__init__.__all__

    #start.start_printer()    # NameError: name 'start' is not defined
