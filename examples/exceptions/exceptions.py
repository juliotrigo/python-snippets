# -*- coding: utf-8 -*-

"""Exceptions."""


class MyException(Exception):

    """General base exception."""

    def __init__(self, value):
        """Assigns the text error."""
        self.value = value

    def __str__(self):
        """Prints the error."""
        return str(self.value)

    def __repr__(self):
        """Representation of the error."""
        return str(self.value)


class IncorrectParameters(MyException):
    """The parameters are incorrect."""
