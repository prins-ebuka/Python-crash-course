import unittest
from city_functions import city_and_country

class NameTestCase(unittest.TestCase):
    """Testing the city_and_country function."""
    def test_city_and_country(self):
        """Testing the city and country function."""
        formatted_name = city_and_country('lagos', 'nigeria', 300)
        self.assertEqual(formatted_name, 'Lagos, Nigeria - population 300' )

if __name__ == '__main__':
    unittest.main()
