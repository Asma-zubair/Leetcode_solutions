class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
        backtrack()
        return res
