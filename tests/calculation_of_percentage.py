import unittest
from modules import calculation_of_percentage
from modules.check_call_module import check

class test_calculation_of_percentage(unittest.TestCase):
    def test_calculation(self):
        input = {
        "count_all_countries": 46981,
        "count_selected_country": 1815
    }
        result = calculation_of_percentage.calculation(input)

        self.assertAlmostEqual(result, 3.8632638726)
        self.assertAlmostEqual(result, 3.86, places = 2)

    def test_calculation_zero(self):
        count = {
        "count_all_countries": 46981,
        "count_selected_country": 1815
    }
        result = calculation_of_percentage.calculation(count)
        self.assertEqual(result, 0, "incorrect result")

    def test_calculation_mark(self):
        count = {
        "count_all_countries": 46981,
        "count_selected_country": 1815
    }
        result = calculation_of_percentage.calculation(count)
        self.assertEqual(result, "!&?./", "incorrect result")

    def test_calculation_negative(self):
        count = {
        "count_all_countries": 46981,
        "count_selected_country": 1815
    }
        result = calculation_of_percentage.calculation(count)
        self.assertAlmostEqual(result, -3.8632638726)
        self.assertAlmostEqual(result, -3.86, places = 2)
