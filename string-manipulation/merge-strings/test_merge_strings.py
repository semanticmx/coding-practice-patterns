from main import Solution


def get_result(word1, word2):
    instance = Solution()
    return instance.merge(word1=word1, word2=word2)


def test_equal_length():
    word1 = "hola"
    word2 = "bola"
    expected = "hboollaa"

    assert get_result(word1, word2) == expected


def test_different_length():
    word1 = "holaaaaa"
    word2 = "bolaa"
    expected = "hboollaaaaaaa"

    assert get_result(word1, word2) == expected


def test_word1_is_first():
    word1 = "ab"
    word2 = "cd"
    expected = "acbd"

    result = get_result(word1, word2)
    assert result == expected
    assert result[0] == word1[0]


def test_word1_is_len_one():
    word1 = "f"
    word2 = "lo que sea"
    expected = "flo que sea"

    assert get_result(word1, word2) == expected