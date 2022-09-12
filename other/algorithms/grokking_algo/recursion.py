
def count_num_items(lst: list) -> int:
    """Write a recursive function to count the number of items in a list."""
    if lst == []:
        return 0
    return 1 + count_num_items(lst[1:])


def find_max(lst: list[int]) -> int:
    """Recursively find the largest number."""
    first, *tail = lst
    if count_num_items(tail) == 1:
        comparator = tail[0]
    else:
        comparator = find_max(tail)
    return first if first > comparator else comparator


def binary_search(searching_for: int, lst: list[int]) -> int | None:
    """Recursively perform binary search"""
    if len(lst) == 2:
        for i in lst:
            if i == searching_for:
                return i
        return None
    mid = lst[len(lst) // 2]
    if lst[mid] == searching_for:
        return lst[mid]
    elif lst[mid] < searching_for:
        return binary_search(searching_for, lst[mid + 1:])
    return binary_search(searching_for, lst[:mid])
