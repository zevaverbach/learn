

def selection_sort(lst: list[int]) -> list[int]:
    srted = []
    mx = lst[0]
    max_idx = 0
    while lst:
        for idx, item in enumerate(lst[1:]):
            if item > mx:
                mx = item
                # since these indices are off by one, having skipped lst[0]
                max_idx = idx + 1
        srted.insert(0, mx)
        del lst[max_idx]

        try:
            mx = lst[0]
        except IndexError:
            pass
        max_idx = 0

    return srted
