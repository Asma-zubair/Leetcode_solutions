# 139. Word Break

## Problem Description (Exact LeetCode Statement)

Given a string `s` and a dictionary of strings `wordDict`, return **true** if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.

---

## Examples

### Example 1

**Input:**

```
s = "leetcode"
wordDict = ["leet", "code"]
```

**Output:**

```
true
```

**Explanation:**
`"leetcode"` can be segmented as `"leet code"`.

---

### Example 2

**Input:**

```
s = "applepenapple"
wordDict = ["apple", "pen"]
```

**Output:**

```
true
```

**Explanation:**
You can reuse words. `"apple"` and `"pen"` appear multiple times.

---

### Example 3

**Input:**

```
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
```

**Output:**

```
false
```

---

## Constraints

* `1 <= s.length <= 300`
* `1 <= wordDict.length <= 1000`
* `1 <= wordDict[i].length <= 20`
* `s` and `wordDict[i]` consist only of lowercase English letters.
* All strings in `wordDict` are **unique**.

---

## Solution

The full implementation is provided in `solution.py`.

