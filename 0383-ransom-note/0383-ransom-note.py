class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for i in magazine:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        
        for r in ransomNote:
            if r not in hashmap or hashmap[r]==0:
                return False
            else:
                hashmap[r]-=1
        return True
