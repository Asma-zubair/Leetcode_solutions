class Solution:
    def findAndReplacePattern(self,words: List[str], pattern:str):
     def wordmatch(word,pattern):
         d1={}
         d2={}
         for i in range(len(pattern)):
            if word[i] in d1 and d1[word[i]]!=pattern[i]:
                return False
            if pattern[i] in d2 and d2[pattern[i]]!=word[i]:
                return False
            d1[word[i]]=pattern[i]
            d2[pattern[i]]=word[i]
         return True
            
     res=[]
     for word in words:
        if wordmatch(word,pattern):
           res.append(word)
     return res