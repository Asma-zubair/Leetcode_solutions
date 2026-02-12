class Solution:
    def longestBalanced(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            freq=[0]*26
            max_freq=0
            distinct=0
            for j in range(i,len(s)):
                index=ord(s[j])-ord("a")

                if freq[index] == 0:
                    distinct+=1
                freq[index]+=1

                max_freq=max(max_freq,freq[index])

                length=j-i+1

                if length==distinct*max_freq:
                    ans=max(length,ans)

        return ans
