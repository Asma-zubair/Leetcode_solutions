# Zigzag Conversion (LeetCode 6)

## 🧩 Problem Overview

The **Zigzag Conversion** problem asks you to rearrange a given string in a zigzag pattern across a specified number of rows, and then read the pattern **row by row** to produce the final string.

This is a classic **string simulation** problem that tests your understanding of patterns and indexing.

---

## 📌 Problem Statement

Given a string `s` and an integer `numRows`, write the string in a zigzag pattern on `numRows` rows.

After writing the characters in zigzag form, **read the characters row-wise** and return the resulting string.

---

## 🔍 Zigzag Pattern Explanation

For example, when `numRows = 3`, the pattern looks like this:

```
P   A   H   N
A P L S I I G
Y   I   R
```

Reading row by row gives:

```
PAHNAPLSIIGYIR
```

---

## 🔢 Input Format

```text
s: string
numRows: int
```

---

## 📤 Output Format

```text
string
```

The zigzag-converted string.

---

## ✅ Example 1

### Input

```text
s = "PAYPALISHIRING"
numRows = 3
```

### Zigzag Layout

```
P   A   H   N
A P L S I I G
Y   I   R
```

### Output

```text
"PAHNAPLSIIGYIR"
```

---

## ✅ Example 2

### Input

```text
s = "PAYPALISHIRING"
numRows = 4
```

### Zigzag Layout

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

### Output

```text
"PINALSIGYAHRPI"
```

---

## ✅ Example 3 (Edge Case)

### Input

```text
s = "A"
numRows = 1
```

### Output

```text
"A"
```

---

## ⚠️ Important Edge Cases

* If `numRows == 1`, return the string as-is.
* If `numRows >= len(s)`, the zigzag pattern is just vertical.

---

## 🛠️ Approach (Simulation)

1. Create a list of strings for each row.
2. Traverse the string character by character.
3. Move **downward** until the last row, then move **upward**.
4. Append characters to the corresponding row.
5. Join all rows at the end.

---

## 🧠 Key Insight

The zigzag movement follows a **down → up → down → up** pattern.

This can be managed using a direction flag:

* `+1` → moving down
* `-1` → moving up

---




