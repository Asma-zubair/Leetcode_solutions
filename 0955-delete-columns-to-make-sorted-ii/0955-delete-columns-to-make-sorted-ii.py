class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
         n=len(strs)
         m=len(strs[0])
         
         tracker=[False]*(n-1)
         deletion=0
         
         for col in range(m):
            bad=False
            for i in range(n-1):
                if not tracker[i] and strs[i][col] >strs[i+1][col]:
                    bad=True
                    break

            if bad:
                deletion+=1
                continue

            for i in range(n-1):
                if not tracker[i] and strs[i][col]<strs[i+1][col]:
                    tracker[i]=True

         return deletion

