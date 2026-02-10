class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        maxL = 0

        for i in range(n):
            even = defaultdict(int)
            odd = defaultdict(int)

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even[nums[j]] += 1
                else:
                    odd[nums[j]] += 1

                # check balanced: distinct even == distinct odd
                if len(even) == len(odd):
                    maxL = max(maxL, j - i + 1)

        return maxL

       