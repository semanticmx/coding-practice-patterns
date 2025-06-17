import unittest
from main import Solution

class TestSolution(unittest.TestCase):

    def test_happy_path(self):
        self.solution = Solution()

        candies = [2, 3, 5, 1, 3]
        extra_candies = 3
        expected = [True, True, True, False, True]
        self.assertEqual(self.solution.execute(candies, extra_candies), expected)

    def test_all_zero_candies(self):
        self.solution = Solution()

        candies = [0, 0, 0]
        extra_candies = 0
        expected = [True, True, True]
        self.assertEqual(self.solution.execute(candies, extra_candies), expected)

    def test_single_kid(self):
        self.solution = Solution()

        candies = [5]
        extra_candies = 10
        expected = [True]
        self.assertEqual(self.solution.execute(candies, extra_candies), expected)

    def test_no_extra_candies(self):
        self.solution = Solution()

        candies = [1, 2, 3]
        extra_candies = 0
        expected = [False, False, True]
        self.assertEqual(self.solution.execute(candies, extra_candies), expected)

if __name__ == "__main__":
    unittest.main()