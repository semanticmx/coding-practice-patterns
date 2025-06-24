import unittest

class Solution:
    def execute(self, word1: str, word2: str) -> str:
        """Merge two strings in an interleaved order.

            A merged string will be returned given two strings.
            If one string is larger than the other one, cut it at
            the last position of the shorter string and append the rest.
        """
        if (len(word1) == 1):
            return word1 + word2

        merged = "".join([i + j for i, j in zip(word1, word2)])
        last_pos = round(len(merged) / 2)
        merged += word1[last_pos:] if len(word1) > last_pos else word2[last_pos:]
        return merged

class TestSolution(unittest.TestCase):
    def test_happypath(self):
        """Cat two strings equal in length

           word1 = "def"
           word2 = "abc"
           :return: "daebfc"
        """
        word1 = "def"
        word2 = "abc"
        instance = Solution()
        result = instance.execute(word1, word2)
        expected = "daebfc"
        self.assertEqual(result, expected)
    
    def test_diff_len(self):
        """Cat two strings different in length

            word1 = "holllaaaa"
            word2 = "pepe"
            :return: "hpoelplelaaaa"
        """
        word1 = "holllaaaa"
        word2 = "pepe"
        instance = Solution()
        result = instance.execute(word1, word2)
        expected = "hpoelplelaaaa"
        self.assertEqual(result, expected)

    def test_word1_one_char(self):
        """Concat strings when word1 length is 1

            word1 = "f"
            word2 = "holA que tal"
            :return: "fholA que tal"
        """
        word1 = "f"
        word2 = "holA que tal"
        instance = Solution()
        result = instance.execute(word1, word2)
        expected = "fholA que tal"
        self.assertEqual(result, expected)

    def test_nums(self):
        """Concat strings that contain numbers

            word1 = "57663"
            word2 = "123941"
            :return: "51726369341"
        """
        word1 = "57663"
        word2 = "123941"
        instance = Solution()
        result = instance.execute(word1, word2)
        expected = "51726369341"
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Concat when a string is empty

            word1 = "Vcbcdjkh"
            word2 = ""
            :return: "Vcbcdjkh"
        """
        word1 = "Vcbcdjkh"
        word2 = ""
        instance = Solution()
        result = instance.execute(word1, word2)
        expected = "Vcbcdjkh"
        self.assertEqual(result, expected)
    
    def test_empty_strings(self):
        """Return when both strings are empty

            word1 = ""
            word2 = ""
            :return: ""
        """
        word1 = ""
        word2 = ""
        instance = Solution()
        result = instance.execute(word1, word2)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()