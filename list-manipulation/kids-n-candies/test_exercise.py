from main import Solution


def get_result(candies, extra_candies):
    instance = Solution()
    return instance.execute(candies, extra_candies)


def test_equal_length():
    candies = [4, 4, 4, 4, 4, ]
    extra_candies = 3
    expected = [True, True, True, True, True, ]

    assert get_result(candies, extra_candies) == expected


def test_happy_path():
    candies = [6, 7, 4, 3, 5, ]
    extra_candies = 2
    expected = [True, True, False, False, True, ]

    assert get_result(candies, extra_candies) == expected


def test_greater_than_or_equal():
    candies = [2, 7, 1, 2, 1, ]
    extra_candies = 6
    expected = [True, True, True, True, True, ]

    assert get_result(candies, extra_candies) == expected
