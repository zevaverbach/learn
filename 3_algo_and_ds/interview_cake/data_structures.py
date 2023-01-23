from __future__ import annotations
from dataclasses import dataclass
import typing

@dataclass
class Node:
    value: typing.Any
    next: Node | None = None


@dataclass
class LinkedList:
    head: Node
    tail: Node | None = None

text = "In the beginning there was darkness."
node = Node(text[0])
exodus = LinkedList(head=node)


for idx, char in enumerate(text):
    try:
        next_node = Node(text[idx + 1])
    except IndexError:
        exodus.tail = node
    else:
        node.next = next_node
        node = next_node


def print_string_from_linked_list(linked_list: LinkedList) -> None:
    next_ = linked_list.head
    while next_:
        print(next_.value)
        next_ = next_.next


def add_char_to_linked_list_string(char: str, position: int, linked_list: LinkedList) -> None:
    count = 0
    node = linked_list.head
    while count < position:
        if node.next is None:
            raise Exception(f'there was an unexpected "None" at {node}\'s .next')
        node = node.next
        count += 1
    former_next = node.next
    node.next = Node(char, next=former_next)
