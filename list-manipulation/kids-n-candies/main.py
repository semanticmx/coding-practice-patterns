class Solution:
    def execute(self, candies, extra_candies):
        """
        O(n^2)
        """
        n = len(candies)
        result = []
        for i in range(n):
            temp = candies[i] + extra_candies
            is_biggest = True
            for j in range(n):
                if temp < candies[j]:
                    is_biggest = False
                    break
            result.append(is_biggest)
        return result
