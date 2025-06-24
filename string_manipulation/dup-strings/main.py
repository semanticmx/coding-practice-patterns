import unittest


class Solution:
    """
    1. Work around the work: Review, PM
    2. Work to get the work: Research, experiment, scope, pitching
    3. Work before the work: Config, setup, service, infra
    4. The work: design, build, docs, test, etc
    """
    def is_integer(self, num)->bool:
        return int(num) == num

    def get_primes(self):
        return [2, 3, 5, 7, 9, 11, ]

    def get_prime_roots(self, max_chars):
        primes = self.get_primes()
        i = 0
        dividend = max_chars
        roots = []
        while i < len(primes) or dividend != 1:
            result = dividend / primes[i]
            is_integer = self.is_integer(result)
            if is_integer:
                dividend = result
                roots.append(primes[i])
            else:
                i += 1

        return roots

    def execute(self, str1: str)->str:
        # find mcd of str1's len
        max_chars = len(str1)
        roots = self.get_prime_roots(max_chars)
        if not roots:
            return ""
        i = 0
        str1_len =  len(str1)
        gcd = ""
        while i < len(roots) and roots[i] * 2 <= str1_len:
            current_root = roots[i]
            multiplier = str1_len // current_root
            divisor = str1[:current_root] * multiplier
            if divisor == str1:
                gcd = str1[:current_root]
                break
            i += 1

        return gcd


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
        str1 = "HOLPHOLHOL"
        instance = Solution()
        result = instance.execute(str1)
        self.assertEqual("", result)

    def test_special_case_one(self):
        """
        str1 = "ABAABAABAABAABAABAABAABA"
        :return: "ABA"
        """
        str1 = "ABAABAABAABAABAABAABAABA"
        instance = Solution()
        result = instance.execute(str1)
        expected = "ABA"

        self.assertEqual(expected, result)

    def test_odd_case(self):
        """
        str1 = "ABCDEABCDEABCDE"
        :return: "ABCDE"
        """
        str1 = "ABCDEABCDEABCDE"
        instance = Solution()
        result = instance.execute(str1)
        expected = "ABCDE"

        self.assertEqual(expected, result)

    def test_roots(self):
        instance = Solution()
        result = instance.get_prime_roots(24)
        self.assertEqual([2, 2, 2, 3], result)

    def test_is_integer(self):
        instance = Solution()
        result = instance.is_integer(24.0)
        self.assertTrue(result)

        result = instance.is_integer(12.0)
        self.assertTrue(result)

        result = instance.is_integer(6.0)
        self.assertTrue(result)

        result = instance.is_integer(3.0)
        self.assertTrue(result)

        result = instance.is_integer(1.5)
        self.assertFalse(result)

    def test_primes(self):
        instance = Solution()
        result = instance.get_primes()
        self.assertEqual([2, 3, 5, 7, 9, 11, ], result)

if __name__ == "__main__":
    unittest.main()
