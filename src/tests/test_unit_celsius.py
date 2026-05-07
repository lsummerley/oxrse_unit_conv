import unittest
from oxrse_unit_conv.units import C, K

class TestCelsius(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(C.si_unit.matches(K))

    def test_basic_conversion(self):
        self.assertEqual(C.to_si(25), 298.15)
        self.assertEqual(C.to_unit(10, K), 283.15)


if __name__ == '__main__':
    unittest.main()