from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        past = Counter(nums)
        future = Counter()

        ans = 0

        for n in nums:
            past[n] -= 1
            target = n * 2

            left = past[target]
            right = future[target]

            ans = (ans + left * right) % MOD

            future[n] += 1

        return ans
