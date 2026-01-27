class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        d1={}
        d2={}
        for i in range(len(pattern)):
                if pattern[i] in d1 and d1[pattern[i]]!=word[i]:
                    return False
                if word[i] in d2 and d2[word[i]]!=pattern[i]:
                    return False
                
                d1[pattern[i]]=word[i]
                d2[word[i]]=pattern[i]
                
        return True