class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        hashmap=defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
         
        ans=[]
        n=len(nums)
        for q in queries:
            value=nums[q]
            indices=hashmap[value]
            if len(indices)==1:
                ans.append(-1)
                continue

            pos=bisect.bisect_left(indices,q)
    
            left=0
            if pos > 0 :
               left=indices[pos-1]
            else:
               left=indices[-1]

            right=0
            if pos < len(indices)-1:
                right=indices[pos+1]
            else:
                right=indices[0]

            d1=abs(q-left)
            d2=abs(q-right)

            dict1=min(d1,n-d1)
            dict2=min(d2,n-d2)

            ans.append(min(dict1,dict2))
        return ans

           
        
            