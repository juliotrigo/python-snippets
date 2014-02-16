# -*- coding: utf-8 -*-

"""Testing moduletodistribute module."""

import unittest

from .moduletodistribute import Greeting


class GreetingTestCase(unittest.TestCase):

    """Greeting class test case."""

    def test_greeting_print(self):
        """greeting_print must print the value provided to __init__."""
        greeting = Greeting('Welcome')
        self.assertEqual(greeting.get_greeting('Julio'), 'Welcome Julio')
