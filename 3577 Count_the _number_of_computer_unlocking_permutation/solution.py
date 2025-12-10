from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD=10**9+7
        n=len(complexity)

        for i in range(1,n):
            if complexity[0]>=complexity[i]:
                return 0

        ans=1
        for i in range(1,n):
            ans=(ans*i)%MOD

        return ans