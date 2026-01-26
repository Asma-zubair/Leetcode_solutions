class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        minimum=float('inf')
        for i in range(1,len(arr)):
             m=arr[i]-arr[i-1]
             minimum=min(m,minimum)

        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==minimum:
                res.append([arr[i-1],arr[i]])
        return res
            


                
