from insertion_sort import insertion_sort

from pytest import fixture as f

@f
def test_data_worst_case():
    return (
    ([2, 1], [1, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
    ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),
    ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
)

@f
def test_data_best_case():
    return (([1, 2], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
)

def test_insertion_sort(test_data_worst_case, test_data_best_case):
    for inp, outp in test_data_worst_case:
        result = insertion_sort(inp)
        assert result == outp
    for inp, outp in test_data_best_case:
        result = insertion_sort(inp)
        assert result == outp
