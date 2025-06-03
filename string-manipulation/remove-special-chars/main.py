from collections import defaultdict


class Solution:
    def convert_to_words(self, text:str)->list:
        # 2.
        # words = text.split()
        # for word in words:
        #    word = word.lower()
        # return words
        # discarded: since it introduces a second loop
        return text.split()

    def execute(self, text:str)->dict:
        words = self.convert_to_words(text=text)
        stats = defaultdict(int)
        for word in words:
            # 1. word = word.lower() [x]
            word = word.lower()
            stats[word] += 1
        return stats
