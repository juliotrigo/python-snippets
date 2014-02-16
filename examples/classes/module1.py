# -*- coding: utf-8 -*-

"""module1 documentation"""


class Class1(object):

    """Class 1 documentation

    New-style classes have been around since Python 2.2.
    You need to make sure you are subclassing from object
    to avoid odd edge cases involving method resolution order, etc.
    This continues to be totally valid in Python 3
    (although unneeded as all classes implicitly inherit from object).
    http://docs.python.org/3/howto/pyporting.html


    '__doc__'
    '__dict__'
    '__module__'
    '__weakref__'

    '__init__'

    '__slots__'
    '__bases__'

    """

    classattr1 = 'a1'
    _classattr2 = 'a2'
    __classattr3 = 'a3'

    def __init__(self, name='name1', surname='surname1'):
        """Constructor Class 1 documentation."""
        self.name = name
        self.surname = surname
        self._attr_private = 1
        self.__attr_mangling = 2

    def method1(self):
        """Method 1 documentation."""
        print('Class 1, Method 1.')
        print('name: ' + self.name)
        print('surname: ' + self.surname)

    def _method2(self):
        """Method 2 documentation."""
        print('Class 1, Method 2.')
        print(self._attr_private)

    def __method3(self):
        """Method 3 documentation."""
        print('Class 1, Method 3.')
        print(self.__attr_mangling)


if __name__ == '__main__':
    print('Class1 name: ' + Class1.__name__)
    print('Class1 doc: ' + Class1.__doc__)
    print('Class1 dir()')
    print(dir(Class1))
    print('Class1__dict__.keys()')
    print(Class1.__dict__.keys())
    print('Class1 __module__: ' + Class1.__module__)
    print(Class1.__weakref__)
    print(Class1.__bases__)

    c1 = Class1('First')

    print('c1 doc: ' + c1.__doc__)
    print('c1 dir()')
    print(dir(c1))
    print('c1 __dict__.keys()')
    print(c1.__dict__.keys())
    print(c1.__class__)

    # Class Attributes
    print(c1.classattr1)
    print(c1._classattr2)
    #print(c1.__classattr3)  #private access
    print(c1._Class1__classattr3)

    # Instance Attributes
    print(c1.name)
    print(c1.surname)
    print(c1._attr_private)
    #print(c1.__attr_mangling)  #private access
    print(c1._Class1__attr_mangling)

    # Methods
    c1.method1()
    c1._method2()
    c1._Class1__method3()
