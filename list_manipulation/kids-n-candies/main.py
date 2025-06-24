from dataclasses import dataclass


@dataclass
class ExerciseOptions:
    result_cache: dict
    candies: list
    result: list
    extra_candies: int = 0
    greatest: int = 0

    def update_result(self, index:int):
        if index in self.result_cache.keys():
            self.result[index] = self.result_cache[index]
            return
        # check if candies + extra_candies is greater than or equal the greatest
        self.result[index] = (self.candies[index] + self.extra_candies) >= self.greatest
        self.result_cache[index] = self.result[index]


class Solution:
    def execute(self, candies: list, extra_candies: int) -> list:
        """

        :param candies:
        :param extra_candies:
        :return:
        """
        options = ExerciseOptions(
            result_cache={},
            candies=candies,
            result=[False] * len(candies),
            extra_candies=extra_candies,
        )
        n = len(options.candies)
        for init in range(n):
            # calculate opposite index based on init value
            end = n - init - 1
            if init <= end:
                options.greatest = max(
                    options.greatest,
                    candies[init],
                    candies[end],
                )

            if init >= end:
                options.update_result(index=init)
                options.update_result(index=end)

        return options.result
