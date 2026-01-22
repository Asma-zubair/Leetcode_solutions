class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic=Counter(s)
        for num in t:
            if num not in dic or dic[num]==0:
                return num
            dic[num]-=1
            
        