class Solution:
    def binaryGap(self, n: int) -> int:
           no=bin(n)[2:]
           last=-1
           max_distance=0

           for i in range(len(no)):
              if no[i]=="1":
                if last != -1 :
                    max_distance=max(max_distance,i-last)
                last=i
            
           return max_distance