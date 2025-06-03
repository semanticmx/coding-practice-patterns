class Solution:
    def merge(self, word1: str, word2: str) -> str:
        """

        """
        if (len(word1) == 1):
            return word1 + word2

        merged = "".join([i + j for i, j in zip(word1, word2)])
        last_pos = round(len(merged) / 2)
        merged += word1[last_pos:] if len(word1) > last_pos else word2[last_pos:]
        return merged


if __name__ == "__main__":
    pass
