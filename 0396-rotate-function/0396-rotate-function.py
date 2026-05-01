class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        n=len(nums)

        F=sum(i*num for i,num in enumerate(nums))
        max_val=F

        for k in range(1,n):
           F=F + total_sum - n* nums[n-k]
           max_val=max(F,max_val)

        return max_val
