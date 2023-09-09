import unittest
from stats import StatFunctions


class FunctionTestMethods(unittest.TestCase):
    bubble_sort_test_array = [-4, 3, 5, 7, 8, 9]

    def test_min(self):
        self.assertEqual(StatFunctions.min_function([2, 4, 6, 1, 2]), 1)

    def test_max(self):
        self.assertEqual(StatFunctions.max_function([2, 4, 6, 1, 2]), 6)

    def test_bubble_sort(self):
        self.assertEqual(StatFunctions.bubble_sort(self.bubble_sort_test_array), sorted(self.bubble_sort_test_array))

    def test_mean(self):
        self.assertEqual(StatFunctions.mean_function([2, 4, 6, 1, 2]), (1 + 2 + 2 + 4 + 6) / 5.0)
        self.assertEqual(StatFunctions.mean_function([2, 4, 4, 4, 5, 5, 7, 9]), 5)

    def test_median_even(self):
        self.assertEqual(StatFunctions.median_function([2, 4, 6, 1, 2, 5]), 3)

    def test_median_odd(self):
        self.assertEqual(StatFunctions.median_function([2, 4, 6, 1, 2]), 2)

    def test_variance(self):
        self.assertEqual(StatFunctions.variance_function([2, 4, 4, 4, 5, 5, 7, 9]), 4)

    def test_standard_deviation(self):
        self.assertEqual(StatFunctions.std_function([2, 4, 4, 4, 5, 5, 7, 9]), 2)

    def test_mad(self):
        self.assertEqual(StatFunctions.mad_function([1, 1, 2, 2, 4, 6, 9]), 1)


if __name__ == '__main__':
    unittest.main()
