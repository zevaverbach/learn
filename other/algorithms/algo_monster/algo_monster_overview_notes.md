# Math Basics

## Sets

### Permutations

Number of permutations for a given set: n!

This is because at every branch, there's one less option, so for n of 3 the total permutations is 3 * 2 * 1.

### Subsets

Number of subsets for a given set: 2^n

This is because for every item there are two options.

## Arithmetic Sequence

A sequence where the difference between each member is consistent.

Sum of an arithmetic sequence:

(sequence[0] + sequence[-1]) * len(sequence)

### Nested Loop Complexity Analysis

n = 10
for (i=0; i<n; i++) {
  for (j=0; j<=i; j++) {
	  doSomething()
	}
}

How many times does `doSomething` run, given `n`?

i = 0, runs = 1
i = 1, runs = 2
i = 2, runs = 3
...
i = 9, runs = 10

(1 + 9) * 10 = 100, so the runtime complexity is n ^ 2

# Modular Arithmetic

def mod(num: int, divisor: int) -> int:
    while num > divisor:
		    num -= divisor
	  return num

MOD is more or less the remainder of integer division.

## It's Distributive

15 MOD 12 is exactly the same as (13 MOD 12) + (2 MOD 12):

13 MOD 12 = 1, 2 MOD 12 is 2, 2 + 1 = 3
15 MOD 12 = 3

## Interview Questions: "divisible"

Given an array of integers, find the two integers whose sum is divisible by 60.

"divisible by 60" == "n % 60 == 0"

so with [30, 20, 150, 110, 200], calling "x % 60" on each yields [30, 20, 30, 50, 20].

Since MOD is distributive, the pairs of members whose sum of MODs is 60 is

((a % 60) + (b % 60)) % 60 = 0

# Runtime Complexity

A server can do roughly 10^8 operations per second (100 million)

## O(1) - "Constant Time"

- hashmap lookup
- array access and update
- pushing and popping elements from a stack
- finding and applying math formula
- typically for n > 10^9

## O(log n)

Grows very slowly.

- binary search
- balanced binary search tree lookup
- processing the digits of a number
- typically for n > 10^8

Example:
```python
n = 100_000_000
while n > 0:
    n // 2
```

## O(n)

- going through linked list/array
- two pointers
- some types of 'greedy'
- tree/graph traversal
- stack/queue
- typically for n <= 10^8

Examples:

```python
i = 0
while i < n:
    i += 1
```

## Other
There's more time complexities but let's continue.

## Exercises
1. 3N + 2N + N --> O(1)
   2n^3 + 5N^2 --> O(1)
   N + log(N) --> O(log n)
   N^2log(N) --> log(n)
   2^N + N^2 --> O(n)
   10 -> O(1)
2. O(N)
3. O(N^2)
4. O(N^2)
5. ?
6. O(log n)


