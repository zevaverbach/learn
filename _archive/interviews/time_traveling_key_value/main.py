"""
TODO: mock time
TODO: test invalid inputs

FEEDBACK:

    - outline a more comprehensive set of tests
        - don't wait for interviewer
        - edge cases
            - more keys
            - more countries
            - future
            - past

"""
import collections
import time

import pytest


class NoSuchCountry(Exception):
    ...



class TimeTravelingKeyValue:

    def __init__(self):
        self._store = collections.defaultdict(list)

    def put(self, key: str, value: str, t: float = None) -> None:
        """
        always called in order of `t`
        """
        t = t or time.time()
        self._store[key].append((t, value))

    def get(self, key: str, t: float) -> str:
        try:
            country = self._store[key]
        except KeyError:
            raise NoSuchCountry
        for timestamp, leader in reversed(country):
            if t >= timestamp:
                return leader



@pytest.fixture
def ttkv():
    return TimeTravelingKeyValue()


@pytest.fixture
def put_leaders(ttkv):
    ttkv.put("United Kingdom", "John Major", 1)
    ttkv.put("United Kingdom", "Boris Johnson", 20)
    ttkv.put("United Kingdom", "Liz Truss", 22)


def test_put(ttkv):
    assert ttkv.put("United States", "Barack Obama") is None


def test_get_john(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 19) == "John Major"


def test_get_boris_a_bit_later(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 21) == "Boris Johnson"


def test_get_boris(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 20) == "Boris Johnson"


def test_get_boris_a_bit_later(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 21) == "Boris Johnson"


def test_get_liz(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 22) == "Liz Truss"


def test_get_liz_a_little_after_put(put_leaders, ttkv):
    assert ttkv.get("United Kingdom", 25) == "Liz Truss"
