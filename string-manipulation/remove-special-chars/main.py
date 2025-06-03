class Solution:
    def convert_to_words(self, text:str)->list:
        return text.split()

    def execute(self, text:str)->dict:
        words = self.convert_to_words(text=text)
        return {}
