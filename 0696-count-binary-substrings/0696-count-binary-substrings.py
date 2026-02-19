class Solution:
    def countBinarySubstrings(self, s: str) -> int:
         prev_length=0
         curr=1
         result=0

         for i in range(1,len(s))  :
            if s[i] == s[i-1] :
                curr+=1
            else:
                result+=min(prev_length,curr)  
                prev_length=curr
                curr=1

         result+=min(prev_length,curr) 
         return result  