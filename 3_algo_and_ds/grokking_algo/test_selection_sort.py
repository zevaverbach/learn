from selection_sort import selection_sort


def test_selection_sort():
    a = [5, 2, 3, 1, 0, 9]
    result = selection_sort(a)
    assert result == [0, 1, 2, 3, 5, 9], result
