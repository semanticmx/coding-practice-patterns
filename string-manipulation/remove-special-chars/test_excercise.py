from main import Solution


def get_result(text:str):
    instance = Solution()
    return instance.execute(text=text)


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

    asset expected == result
