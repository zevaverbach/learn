# Stack

First in, last out (FILO).	

Three Operations:
- push
- peek (look at the top of the stack)
- pop

# Queue

First in, first out (FIFO).

Three operations:

- push
- peek 
- pop

# Hashmap

A good hash function
- has low time complexity
- has low probability of hash collision
- all possible values are utilized about equally

## Naive Implementation

Create a fixed length array.

For each key:value pair, hash the key and put the value at the index equal to the hash.

Drawback: If there's a hash collision, the existing value will simply be overwritten.

## Separate Chaining

Same as the naive implementation, only instead of storing the value at the array's index, you create a linked list of key value pairs.

## Efficiency

- insert
  - O(n / k) where n is number of entries in the hash table, k is the length of the array
	- worst-case O(n), if every value is stored at the same index (same hash)
- lookup: O(1)

In modern programming languages, hashmaps are dynamically sized and have O(1) for all of lookup, insert and delete

# Python Basic Data Structures

## Linked List

```python
from __future__ import annotations
import typing as t

class LinkedListNode:
    def __init__(self, val: t.Any, next_: t.Optional["LinkedListNode"] = None):
		    self.val = val
				self.next = next_
```

### Efficiency
- append O(1)
- find O(n)

## Stack (list)
- push, pop, size, top: O(1)

## Queue (collections.deque)
- append, popleft, pop, size: O(1)

## Hash Set
- lookup, add, discard: O(1)
