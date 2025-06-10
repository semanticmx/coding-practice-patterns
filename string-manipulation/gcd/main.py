import unittest


def _cleaned_data(*args)->list:
    cleaned = []
    for arg in args:
        class_name = arg.__class__.__name__
        match class_name:
            case "str":
                cleaned.append(arg)
            case "int":
                cleaned.append(str(arg))
            case "list":
                cleaned.append("".join(arg))
            case "dict":
                cleaned.append("".join(arg.values()))
            case "object":
                cleaned.append(str(arg))
            case "bool":
                cleaned.append("1" if arg else "0")
            case _:
                cleaned.append(str(arg))
    return cleaned



def gcd_from_strings(str1: str, str2: str)->bool:
    """
    1. Work around the work: review projects
    2. Work to get the work: research
    3. Work before the work: setup
    4. The work: test, fix, feedback
    5. Work between the work: iteration
    6. Work beyond the work: change | nice to have
    7. Work outside the work: bugs
    8. Work after the work: support

    if str1 divides by GCD str2 then return True

    str1: divisor string
    str2: string to be divided
    :returns bool
    """
    pass


class GcdTestCase(unittest.TestCase):
    def test_happypath(self):
        str1 = "ABC"
        str2 = "ABCABC"
        result = gcd_from_strings(str1, str2)
        self.assertTrue(result)

    def test_is_false(self):
        str1 = "ABC"
        str2 = "ABCABCD"
        result = gcd_from_strings(str1, str2)
        self.assertFalse(result)

    def test_shorter_string(self):
        str1 = "ABC"
        str2 = "ABCAB"
        result = gcd_from_strings(str1, str2)
        self.assertFalse(result)

    def test_is_same(self):
        str1 = "ABC"
        str2 = "ABC"
        result = gcd_from_strings(str1, str2)
        self.assertTrue(result)

    def test_invalid(self):
        str1 = "A"
        str2 = "ABC"
        result = gcd_from_strings(str1, str2)
        self.assertTrue(result)

    def test_greater_divider(self):
        str1 = "ABCD"
        str2 = "ABC"
        result = gcd_from_strings(str1, str2)
        self.assertFalse(result)

    def test_empty_divider(self):
        str1 = ""
        str2 = "ABCABC"
        result = gcd_from_strings(str1, str2)
        self.assertFalse(result)

    def test_empty_str2(self):
        str1 = "ABC"
        str2 = ""
        result = gcd_from_strings(str1, str2)
        self.assertFalse(result)

    def test_recoverable(self):
        str1 = 31
        str2 = "313131"
        c1, c2 = _cleaned_data(str1, str2)
        self.assertEqual("31", c1)
        self.assertEqual("313131", c2)

        str1 = True
        str2 = "111"
        c1, c2 = _cleaned_data(str1, str2)
        self.assertEqual("1", c1)
        self.assertEqual("111", c2)

        str1 = ["A", "B", "C"]
        str2 = "ABCABC"
        c1, c2 = _cleaned_data(str1, str2)
        self.assertEqual("ABC", c1)
        self.assertEqual("ABCABC", c2)

        str1 = '\x41\x42'
        str2 = "ABABAB"
        c1, c2 = _cleaned_data(str1, str2)
        self.assertEqual("AB", c1)
        self.assertEqual("ABABAB", c2)

        class Divider():
            def __str__(self):
                return "ABCD"
        instance = Divider()
        str1 = instance
        str2 = "ABCDABCDABCD"
        c1, c2 = _cleaned_data(str1, str2)
        self.assertEqual("ABCD", c1)
        self.assertEqual("ABCDABCDABCD", c2)


if __name__ == "__main__":
    unittest.main()
