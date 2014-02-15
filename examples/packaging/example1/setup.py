# -*- coding: utf-8 -*-

"""moduletodistribute setup.

    distutils / setuptools example.

    http://docs.python.org/2/distutils/index.html
    http://www.python.org/dev/peps/pep-0314/
    https://pypi.python.org/pypi?:action=list_classifiers

    https://pythonhosted.org/setuptools/index.html
    http://svn.python.org/projects/sandbox/trunk/setuptools/setuptools.txt

    $ python setup.py sdist
    $ python setup.py install
    $ python setup.py --install-lib=./app-packages
    $ python setup.py --name
    $ python setup.py bdist

"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import moduletodistribute

setup(
    name='moduletodistribute',
    version=moduletodistribute.__version__,
    author='Julio Vicente Trigo Guijarro',
    author_email='',
    url='https://github.com/juliotrigo/python-snippets',
    description='A module distribution example.',
    long_description=moduletodistribute.__doc__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='BSD',
    py_modules=['moduletodistribute'],
    zip_safe=False,

    #packages=[],
    #package_data={'': ['LICENSE', 'README.md']},
    #data_files=[],
    #package_dir={},
    #include_package_data=True,
    #test_suite='',
    #install_requires=[],
    #extras_require={},
    #platforms='any',
    #cmdclass={},
    #entry_points="""""",
    #scripts=[],
)
