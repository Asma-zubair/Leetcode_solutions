class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
         actual={}
         made={}

         for i in range(len(s)):
            if s[i] in actual and actual[s[i]] != t[i]:
                return False
            if t[i] in made and made[t[i]] != s[i]:
                return False
            
            actual[s[i]] = t[i]
            made[t[i]] = s[i]
         return True
        