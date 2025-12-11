class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        maxlen = 1

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1, l + 1

        for i in range(len(s)):
            len1, start1 = expand(i, i)
            len2, start2 = expand(i, i + 1)

            if len1 > maxlen:
                maxlen = len1
                start = start1

            if len2 > maxlen:
                maxlen = len2
                start = start2

        return s[start:start + maxlen]
