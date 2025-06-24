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


def test_special_chars_on_bounds():
    text = "lead Cow baby! success cow bigger $green cake"
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


def test_inner_special_chars():
    text = "l3!!4d Cow baby! success cow b1,gg3r $gr33.n cake"
    result = get_result(text=text)
    expected = {
        "l3!!4d": 1,
        "cow": 2,
        "baby": 1,
        "success": 1,
        "b1,gg3r": 1,
        "gr33.n": 1,
        "cake": 1,
    }

    assert result == expected


def test_clean_word():
    word = "!!baby!"
    instance = Solution()
    cleaned = instance.strip_nonalnum(word=word)

    assert cleaned == cleaned


def test_final_boss():
    text = "\"l3\"4d\"\"\" Cow !!baby! succ..ess cow #b1,gg3,r $gr33.n# cake"
    result = get_result(text=text)
    expected = {
        "l3\"4d": 1,
        "cow": 2,
        "baby": 1,
        "succ..ess": 1,
        "b1,gg3,r": 1,
        "gr33.n": 1,
        "cake": 1,
    }

    assert result == expected
