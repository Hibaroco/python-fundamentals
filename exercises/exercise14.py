# 11-1 City, Country

import unittest

from city_functions import city_country

class CityTest(unittest.TestCase):

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()

#11-2

# I am running out of time, and I want to be sure to get the quiz in. Sorry I will just turn in this part of the work