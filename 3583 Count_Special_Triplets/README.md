# **LeetCode 3583 — Count Special Triplets**

## **📝 Problem Description**

You are given an integer array `nums`.

A **special triplet** is a triplet of indices `(i, j, k)` such that:

- `0 ≤ i < j < k < nums.length`
- `nums[i] == nums[j] * 2`
- `nums[k] == nums[j] * 2`

Your task is to return the **total number of special triplets** in the array.

A triplet is considered special only when the **first** and **third** values are **exactly double** the **middle** value.

---

## **📘 Examples 1**

Input: nums = [6, 3, 6]
Output: 1

Explanation:
The only special triplet is (0, 1, 2):
nums[0] = 6 = 3 * 2
nums[2] = 6 = 3 * 2

---
### **Example 2**
Input: nums = [8, 4, 2, 8, 4]
Output: 2

Explanation:
Two special triplets exist:

(0, 1, 3) → (8, 4, 8)
(1, 2, 4) → (4, 2, 4)

In both cases, first and third elements are double the middle element.

---
