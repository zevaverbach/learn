from recursion import count_num_items, find_max, binary_search


def test_count_num_items():
    items = [1,2,3, 4, 5, 6, 7]
    result = count_num_items(items)
    assert result == len(items), result


def test_find_max():
    items = [8, 7, 6, 5, 4, 1]
    result = find_max(items)
    assert result == max(items), result


def test_binary_search():
    items = [1,2,3, 4, 5, 6, 7]
    assert binary_search(3, items) == 3
    assert binary_search(7, items) == 7
    assert binary_search(2, items) == 2
    assert binary_search(0, items) is None
