class Solution:
    def merge(self, word1: str, word2: str) -> str:
        """
        1. Requirements
        2. DocTest
        3. Edge Cases
        4. Approach

        1.Requeriments
            - Merge two strings in alternative order, starting with the first string
            - If some string is longer we append the remaining to the end of the merged string
            - While has characters in both strings we alternative the order and add it in order
        in the merged string
            - Just are valid lower case letters
            - Just accept words in english
            - The length of two words needs be in the range [1-100]

        2.DocTest
        s = Solution()

        s.mergeCarmen("abc", "xyz")
        output: sadefigo
        s.mergeCarmen("asd", "werc")
        output: awsedrc
        s.mergeCarmen("tqwrd", "ae")
        output: taqewrd
        s.mergeCarmen("añewr","dewf")
        output: Error invalid character
        s.mergeCarmen("AEio", "swrf")
        output: Error only lowercase letters

        Edge cases
            - The strings dont be in the admited range [1-100]
            - The strings not only contains english characters
            - The strings not only contain lowercase letters
            - The length of the strings are diferent
            - Bhot strings contains the just only one character


        Aproach
            - Validate that the strings contains only english characters
            - Validate that the length of the strings are in the range [1-100]
            - Validate thet the strings only has lowercase letters
            - Return an error if dont pass some validations
            - Review what string has the shortest length
            - Use the shorter  word for iterate betwen the words
            - Start with the first word taking each character and  save it in the
            merged string after that, take the second word and save each character into the merged
            string, repit until shorter length
            - If some word has more letter we going to take the remaind and  append in the merged string
            - Rerturned the merged string

        """
        print(f"{word1=}")
        print(f"{word2=}")
        # O(c)
        merged = ""

        # @TODO: operador ternario?
        # SRP: ver cuál es la palabra más corta
        shorter = word1
        if len(word1) > len(word2):
            shorter = word2
        print(f"{shorter=}")

        # SRP: Caso especial, unir shorter cuando es
        #      un solo caracter
        # 2x + 4 = 2 (x + 2)
        if (len(word1) == 1):
            # @TODO: se usa merged?
            merged += word1 + word2
            print(f"Optimized {merged=}")
            return merged

        print(f"This is the shortest word: {shorter=}")
        # O(n)
        # SRP: mezclar los caracters hasta el más corto
        for i, j in zip(word1, word2):
            merged += i + j
        print(f"merged step 1 {merged=}")

        # multiplicar un string
        # merged y word1 y word2
        # SRP: Unir el resto
        #   Sub-SRP: Identificar posición del resto
        #   Sub-SRP: Identificar el resto de caracteres
        # [start:end-not-inclusive]
        # [10:]
        res = word2[len(shorter):]
        if len(word2 * 2) == len(merged):
            res = word1[len(shorter):]

        print(f"resto {res=}")
        print(merged + res)
        return merged + res


if __name__ == "__main__":
    pass
