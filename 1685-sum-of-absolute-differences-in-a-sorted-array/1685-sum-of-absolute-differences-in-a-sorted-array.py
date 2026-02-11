class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
         n=len(nums)
         prefix_sum=0
         total_sum=sum(nums)
         result=[0]*n
         for i in range(n):
            current=nums[i]

            left= i*current-prefix_sum

            right=(total_sum - prefix_sum - current) - current * (n - i - 1) 

            result[i]= left + right

            prefix_sum += current

         return result