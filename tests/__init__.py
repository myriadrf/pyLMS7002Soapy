import unittest
import tests.test_lms

def test_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_lms)
    return suite
