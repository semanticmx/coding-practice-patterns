class Solution:
    def merge(self, word1: str, word2: str) -> str:
        """
        1. Requirements
            - Merge two strings by adding letters in alternating order, starting with word1.
            - If one string is longer, append the remaining characterers at the end.
            - The length of each input string must be at least 1 and at most 100 characters.
            - Both strings consist only of lowercase English letters.
        2. DocTest
            >>> s = Solution()
            >>> s.mergeGeorge("abc", "xyz")
            'axbycz'
            >>> s.mergeGeorge("ab", "pqrs")
            'apbqrs'
            >>> s.mergeGeorge("your", "sw")
            'ysowur'
            >>> s.mergeGeorge("", "xyz")
            Traceback (most recent call last):
                ...
            ValueError: Both strings must have between 1 and 100 characters.
            >>> s.mergeGeorge("xyz", "")
            Traceback (most recent call last):
                ...
            ValueError: Both strings must have between 1 and 100 characters.
            >>> s.mergeGeorge(123, "fail")
            TypeError: 'int' object is not subscriptable
        3. Edge Cases
            - One or both input strings are empty (should print an Error).
            - String of different lengths.
            - String with only one character.
            - All characters are the same.
            - One string is exactly 100 characters.
            - One string is longer than 100 characters.
            - The value of one or both inputs are not String types.
            - Some characers are not in lowercase.
            - One or both words are not in ascii English.
        4. Approach
            - First, validate that both input strings have valid lengths (1-100)
            - Use a loop to iterate through the longest string.
            - Append characters from word1 alternately, if present.
            - Join the characters into a string and return it.
        """
        pass


if __name__ == "__main__":
    pass
