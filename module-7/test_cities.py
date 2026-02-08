import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        """Does Santiago, Chile work?"""
        formatted = city_country("Santiago", "Chile")
        self.assertEqual(formatted, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()
