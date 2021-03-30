#!/usr/bin/python3
""" aaaa """

import pep8
import unittest


class test_pep8aa(unittest.TestCase):
    """ testingggggggggggggggggggggggggg """
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
