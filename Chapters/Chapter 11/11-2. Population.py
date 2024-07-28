import unittest
from city_functions import full_location


class CityTests(unittest.TestCase):
    def test_full_location_string_is_proper(self):
        """ Will the string be properly concatenate? """
        location_full_string = full_location("Santiago", "Chile")
        self.assertEqual(location_full_string, "Santiago, Chile")
