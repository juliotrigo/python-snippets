# -*- coding: utf-8 -*-

"""General statements.

Created on 9 Feb 2013

@author: juliotrigo

The from statement is an assignment to names in the importer's scope
(a name-copy operation, not a name aliasing).
The implications of this are the same as for all assignments in Python.
"""

import examples.packages.module3 as module3
import examples.packages.module4 as module4
import examples.modules.internals as internals
import examples.modules.module5 as module5
import examples.modules.module6 as module6
import examples.modules.importermod5 as importermod5
import examples.modules.importermod6 as importermod6

if __name__ == '__main__':
    print("\n***** packages *****")
    module3.module1_access()
    module4._not_public()
    print("********************")
    
    print("\n***** modules *****")
    print("--importermod5.actions()--")
    importermod5.actions()
    print("--internals--")
    internals.actions()
    print("...importermod5...")
    print(importermod5.__dict__["module5"])
    print(importermod5.__dict__["y"])
    print(importermod5.__dict__["printer6"])
    print("...importermod6...")
    print(importermod6.__dict__["module6"])
    print(importermod6.__dict__["x"])
    print(importermod6.__dict__["printer5"])
    print("...module5...")
    print(module5)
    print(module5.__dict__["x"])
    print(module5.__dict__["printer5"])
    print("...module6...")
    print(module6)
    print(module6.__dict__["y"])
    print(module6.__dict__["printer6"])
    
    print("...some modifications...")
    importermod5.__dict__["module5"].x = "Other value 5"
    importermod5.__dict__["y"] = "Other value 6"
    importermod5.__dict__["printer6"] = None
    
    print("...importermod5...")
    print(importermod5.__dict__["module5"])
    print(importermod5.__dict__["y"])
    print(importermod5.__dict__["printer6"])
    print("...module5...")
    print(module5)
    print(module5.__dict__["x"])
    print(module5.__dict__["printer5"])
    print("...module6...")
    print(module6)
    print(module6.__dict__["y"])
    print(module6.__dict__["printer6"])
    print("********************")