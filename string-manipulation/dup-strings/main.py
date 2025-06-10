import unittest


class Solution:
    """
    1. Work around the work: Review, PM
    2. Work to get the work: Research, experiment, scope, pitching
    3. Work before the work: Config, setup, service, infra
    4. The work
    """
    def execute(self, str1: str)->str:
        return ""


class TestSolution(unittest.TestCase):
    def test_happypath(self):
        """
        Find the MCD of str1, such that a substring of str1 can exactly divide str1
        str1 = ""
        :return: "ABC"

        """
        str1 = "ABCABCABCABCABCABC"
        instance = Solution()
        result = instance.execute(str1)
        expected = "ABC"

        self.assertIn(result, str1)
        self.assertEqual(expected, result)
        self.assertNotIn("ABCA", result)
        self.assertListEqual(["A"], list(result[0]))
        self.assertListEqual(["B"], list(result[1]))
        self.assertListEqual(["C"], list(result[2]))

    def test_invalid_mcd(self):
        """
        str1 = "holamundoholaholaholaholaholaholahola"
        :return: ""
        :return:
        """
        str1 = "holamundoholaholaholaholaholaholahola"
        instance = Solution()
        result = instance.execute(str1)
        self.assertEqual("", result)


if __name__ == "__main__":
    unittest.main()
