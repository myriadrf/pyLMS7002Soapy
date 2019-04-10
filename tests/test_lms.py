import os
import sys
import unittest

from pyLMS7002Soapy import pyLMS7002Soapy as pyLMS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestLMS(unittest.TestCase):

    def test_sdr(self):
        # This is where we would test the SDR device
        cond = pyLMS.pyLMS7002Soapy
        self.assertEqual(type(cond), type)
        print("The class type is there")


if __name__ == "__main__":
    unittest.main()
