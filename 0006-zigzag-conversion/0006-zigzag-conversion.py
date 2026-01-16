class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if  numRows==1 or numRows>=len(s):
            return s

        ans=[""]*numRows
        starting=0
        goingdown=False

        for ch in s:
            ans[starting]+=ch

            if starting==0 or starting==numRows-1:
                goingdown=not goingdown

            if goingdown:
                starting+=1
            else:
                starting-=1
        return "".join(ans)