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

"""
create State name="Montevideo"
create City name="Montevideo"
create State name="Canelones"
create City name="Canelones"
create State name="Maldonado"
create City name="Maldonado"
create State name="Melo"
create City name="Cerro Largo"
create State name="Lavalleja"
create City name="Minas"
create State name="Flores"
create City name="Trinidad"
"""
