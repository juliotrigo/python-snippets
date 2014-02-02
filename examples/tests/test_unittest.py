# -*- coding: utf-8 -*-

"""unittest module behaviour.

Usage:
$ python -m unittest discover
$ python -m unittest
$ python -m unittest -v
$ python -m unittest examples.tests.test_unittest
$ python -m unittest examples.tests.test_unittest.UnittestTestCase
$ python -m unittest examples.tests.test_unittest.UnittestSkippedTestCase

Using nose:
$ nosetests
$ nosetests --verbosity=3
$ nosetests --verbosity=3 --with-coverage

"""

import unittest

SKIP_TESTS = True


class UnittestTestCase(unittest.TestCase):

    """Unittest class."""

    def setUp(self):
        """Set up method."""
        #print('setUp...')
        pass

    def tearDown(self):
        """Tear down method."""
        #print('tearDown...')
        pass

    def test_unittest_1(self):
        """Test 1."""
        self.assertTrue(1, 'Test passed.')

    def test_unittest_2(self):
        """Test 2."""
        pass                        # Test passed

    @unittest.skip('demonstrating skipping')
    def test_unittest_3(self):
        """Test 3."""
        self.assertTrue(0, 'TODO')

    @unittest.skipIf(SKIP_TESTS, 'demonstrating skipping')
    def test_unittest_4(self):
        """Test 4."""
        self.assertTrue(0, 'TODO')

    @unittest.expectedFailure
    def test_unittest_5(self):
        """Test 5."""
        self.assertTrue(0, 'TODO')

    def test_unittest_6(self):
        """Test 6."""
        self.assertTrue(0, 'TODO')  # failure


@unittest.skip("showing class skipping")
class UnittestSkippedTestCase(unittest.TestCase):

    """Unittest skipped class."""

    def test_unittest_skipped_1(self):
        """Test skipped 1."""
        self.assertTrue(0, 'TODO')

if __name__ == '__main__':
    unittest.main()
