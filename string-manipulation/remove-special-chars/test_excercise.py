from main import Solution


def get_result(text:str):
    instance = Solution()
    return instance.execute(text=text)


def test_returns_a_dict():
    text = "lead cow baby success pink bigger green cake"
    result = get_result(text=text)

    assert isinstance(result, dict)


def test_convert_text_to_words():
    text = "lead cow baby success pink bigger green cake"
    instance = Solution()
    result = instance.convert_to_words(text)
    expected = [
        "lead",
        "cow",
        "baby",
        "success",
        "pink",
        "bigger",
        "green",
        "cake",
    ]

    assert result == expected


def test_happy_path():
    text = "lead cow baby success pink bigger green cake"
    result = get_result(text=text)
    expected = {
        "lead": 1,
        "cow": 1,
        "baby": 1,
        "success": 1,
        "pink": 1,
        "bigger": 1,
        "green": 1,
        "cake": 1,
    }

    assert result == expected


def test_uppercases():
    text = "lead Cow baby success cow bigger green cake"
    result = get_result(text=text)
    expected = {
        "lead": 1,
        "cow": 2,
        "baby": 1,
        "success": 1,
        "bigger": 1,
        "green": 1,
        "cake": 1,
    }

    assert result == expected
