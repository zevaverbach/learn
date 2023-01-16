"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# def main(s: str) -> bool:
#     s = "".join(char for char in s if char.isalnum()).lower()
#     if len(s) == 0:
#         return True
#     return s[::-1] == s


# def main(s: str) -> bool:
#     filtered = "".join(char.lower() for char in s if char.isalnum())
#     middle_index = None
#     length = len(filtered)
#     if length % 2:
#         middle_index = int((length - 1) / 2)
#     for idx in range(length):
#         if middle_index and middle_index == idx:
#             continue
#         if filtered[idx] != filtered[-(idx + 1)]:
#             return False
#     return True


def main(s: str) -> bool:
    filtered = "".join(char.lower() for char in s if char.isalnum())



def test_one():
    assert main("H") is True


def test_two():
    assert main("hi") is False


def test_nums_and_spaces():
    assert main("a9 89a ") is True


def test_invalid_chars():
    assert main("19.") is False


def test_2_invalid_chars():
    assert main("1 9.") is False


def test_3_invalid_chars():
    assert main("1 9.a") is False


def test_uppercase():
    assert main("abbA") is True


def test_plain():
    assert main("fartraf") is True


def test_10():
    assert main("0P") is False
