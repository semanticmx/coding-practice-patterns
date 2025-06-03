from collections import defaultdict


class Solution:
    def strip_nonalnum(self, word):
        """
        $green => green
        """
        # .isalnum(): bool
        # "asd".isalnum() => True
        # "#asd".isalnum() => False
        # short-circuit function
        if word.isalnum():
            return word

        cleaned = word
        if not word[0].isalnum():
            cleaned = word[1:]

        if not cleaned[-1].isalnum():
            # python ranges are [0:6)
            cleaned = cleaned[:-1]

        return cleaned

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
            word = self.strip_nonalnum(word)
            stats[word] += 1
        return stats
