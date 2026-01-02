class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        n=len(s)
        INTMIN=-2**31
        INTMAX=2**31-1
        sign=1
        num=0


        while i<n and s[i]==" ":
            i+=1


        if i<n and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
              sign=-1
            i+=1
        

        while i<n and s[i].isdigit():
            digit=ord(s[i])-ord('0')
            num=num*10+digit

            if sign*num <= INTMIN:
                return INTMIN
            if sign*num >= INTMAX:
                return INTMAX
            i+=1
        return num*sign


