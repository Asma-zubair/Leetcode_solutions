# 3577. Count the Number of Computer Unlocking Permutations

## Problem Description (Exact LeetCode Statement)

You are given an array `complexity` of length `n`.

There are `n` locked computers in a room with labels from `0` to `n - 1`. The computer labeled `0` is initially unlocked.

To unlock computer `i`, you can use any previously unlocked computer `j` such that **`j < i` and `complexity[j] < complexity[i]`**.

Return the **number of permutations** of `[0, 1, ..., n - 1]` that represent a valid order in which all computers can be unlocked. Since the answer may be large, return it modulo **10^9 + 7**.

---

## Examples

### Example 1

**Input:**

```
complexity = [1, 2, 3]
```

**Output:**

```
4
```

**Explanation:**
Valid permutations are:

```
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[2, 0, 1]
```

Each computer can be unlocked using a previously unlocked computer with a smaller index and smaller complexity.

---

### Example 2

**Input:**

```
complexity = [2, 1]
```

**Output:**

```
1
```

**Explanation:**
Only permutation `[0, 1]` is valid.

---

## Solution

The implementation is provided in `solution.py`.
