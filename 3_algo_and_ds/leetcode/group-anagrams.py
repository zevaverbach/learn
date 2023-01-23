"""
https://leetcode.com/problems/group-anagrams/

Given an array of lowercase strings strs, group the anagrams together. You can return the answer in any order.

"""
import collections
import string

import pytest


class EmptyInput(Exception):
    ...


# def group_anagrams(strs: list[str]) -> list[list[str]]:
#     if not strs:
#         raise EmptyInput
#     groups = collections.defaultdict(list)
#     for st in strs:
#         groups["".join(sorted(st))].append(st)
#     return list(groups.values())

# def group_anagrams(strs: list[str]) -> list[list[str]]:
#     if not strs:
#         raise EmptyInput

#     def make_charmap(a_string: str) -> tuple[int, ...]:
#         c = collections.Counter(a_string)
#         charmap_list = []
#         for char in string.ascii_lowercase:
#             if char in c:
#                 charmap_list.append(c[char])
#             else:
#                 charmap_list.append(0)
#         return tuple(charmap_list)

#     groups = collections.defaultdict(list)
#     for st in strs:
#         groups[make_charmap(st)].append(st)
#     return list(groups.values())


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of lowercase strings strs, group the anagrams together.
    """
    if not strs:
        raise EmptyInput

    ORD_A = ord("a")
    groups = collections.defaultdict(list)

    for st in strs:
        hash_of_chars = [0] * 26
        for char in st:
            pos = ord(char) - ORD_A
            hash_of_chars[pos] += 1
        groups[tuple(hash_of_chars)].append(st)
    return list(groups.values())


def test_group_anagrams_one_single_char_entry():
    assert group_anagrams(["a"]) == [["a"]]


def test_group_anagrams_one_zero_char_entry():
    assert group_anagrams([""]) == [[""]]


def test_group_anagrams_empty_input():
    with pytest.raises(EmptyInput):
        group_anagrams([])


def test_group_anagrams_valid():
    assert group_anagrams(sorted(["eat","tea","tan","ate","nat","bat"])) == sorted([["bat"], ["nat","tan"], ["ate","eat","tea"]])


def test_group_anagrams_no_valid_anagrams():
    assert group_anagrams(["eat","team","bait","nat","bat"]) == [['eat'], ['team'], ['bait'], ['nat'], ['bat']]
