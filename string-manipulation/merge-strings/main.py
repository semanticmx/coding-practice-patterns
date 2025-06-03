class Solution:
    def merge(self, word1: str, word2: str) -> str:
        """
        word1:  [a|b|c|d|e|]
        word2:  [a|b|c|d|e|f|g|h|i|j|k|l|m|n]
        merged: [a|a|b|b|c|c|d|d|e|e]
              : [a|a|b|b|c|c|d|d|e|e|f|g|h|i|j|k|l|m|n]
        """
        if (len(word1) == 1):
            return word1 + word2

        merged = "".join([i + j for i, j in zip(word1, word2)])
        last_pos = round(len(merged) / 2)
        word1[last_pos:] if len(word1) > last_pos else word2[last_pos:]
        return merged


if __name__ == "__main__":
    pass
