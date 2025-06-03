from collections import defaultdict


class Solution:
    def strip_nonalnum(self, word):
        """
        $green => green
        !!baby! => baby
        """
        # .isalnum(): bool
        # "asd".isalnum() => True
        # "#asd".isalnum() => False
        # short-circuit function
        # O(n^2)
        if word.isalnum():
            return word

        # O(2n) - storage complexity
        chars = list(word)
        # !!baby!
        # !baby!
        # baby!
        # O(n)
        while not chars[0].isalnum():
            del chars[0]

        # O(n)
        while not chars[-1].isalnum():
            del chars[-1]

        # O(n)
        return "".join(chars)

    def convert_to_words(self, text:str)->list:
        # O(n)
        # 2.
        # words = text.split()
        # for word in words:
        #    word = word.lower()
        # return words
        # discarded: since it introduces a second loop
        return text.split()

    def execute(self, text:str)->dict:
        # O(n)
        words = self.convert_to_words(text=text)
        # O(c)
        stats = defaultdict(int)
        # O(n)
        for word in words:
            # 1. word = word.lower() [x]
            # O(n)
            word = word.lower()
            # O(2n + n^2)
            word = self.strip_nonalnum(word)
            # O(c)
            stats[word] += 1
        # O(n^3)
        return stats
