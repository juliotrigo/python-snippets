# -*- coding: utf-8 -*-

"""Example of module to distribute."""

__version__ = '1.0.0'


class Greeting(object):

    """Manages greetings."""

    def __init__(self, greeting):
        """Initializes the greeting."""
        self.greeting = greeting

    def get_greeting(self, name):
        """Prints the greeting."""
        return self.greeting + ' ' + name
