"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""


def encode(strs: list[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    return "TOKEN".join(strs)
    

def decode(s: str) -> list[str]:
    """Decodes a single string to a list of strings.
    """
    return s.split("TOKEN")



def test_one():
    assert decode(encode(["","4 "])) == ["","4 "]
