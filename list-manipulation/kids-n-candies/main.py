class Solution:
    def execute(self, candies, extra_candies):
        """
        O(2n)
        obtener el mayor de todos
        """
        greatest = max(candies)
        result = []
        for i in range(len(candies)):
            result.append(False)
            if (candies[i] + extra_candies) >= greatest:
                result[i] = True
        return result
