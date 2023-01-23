import functools
import time
import typing as t

import rich


T = t.TypeVar('T')


@functools.total_ordering
class ComparableChar:
    def __init__(self, char: str | int):
        self.char = char
        if isinstance(char, str):
            self.val: int = ord(char)
        else:
            self.val: int = char

    def __gt__(self, other: "ComparableChar"):
        return self.val > other.val

    def __repr__(self):
        return str(self.char)


def insertion_sort(lst: list[T]) -> list[T]:
    if not isinstance(lst[0], (str, int)):
        raise TypeError
    list_concrete: list[str] | list[int] = lst
    the_list = [ComparableChar(i) for i in list_concrete]
    for idx, item in enumerate(the_list):
        index = idx
        while index > 0 and item < the_list[index - 1]:
            swap(the_list, index)
            index -= 1
            time.sleep(.1)
            rich.print("".join(list(map(str, the_list))))

    if isinstance(lst[0], int):
        attr = "val"
    else:
        attr = "char"
    return [getattr(i, attr) for i in the_list]


def swap(lst: list[ComparableChar], index: int) -> None:
    earlier = lst[index - 1]
    later = lst[index]
    lst[index] = earlier
    lst[index - 1] = later


def test():
    letters = list("I N S E R T I O N S O R T".replace(" ", ""))
    sorted_letters: list[str] = insertion_sort(letters)
    assert "".join(sorted_letters) == "EIINNOORRSSTT"

    numbers = [5, 4, 10, 12, 15, 0]
    sorted_numbers = insertion_sort(numbers)
    assert sorted_numbers == [0, 4, 5, 10, 12, 15]


if __name__ == "__main__":
    test()
