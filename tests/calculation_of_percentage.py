import unittest
from modules import calculation_of_percentage


class TestCalculationOfPercentage(unittest.TestCase):
    def test_calculation(self):
        count = {
            "count_all_countries": 46981,
            "count_selected_country": 1815
        }
        result = calculation_of_percentage.calculation(count)
        self.assertAlmostEqual(result, 3.8632638726)
        self.assertAlmostEqual(result, 3.86, places=2)
        self.assertAlmostEqual(result, 3.863, places=3)
