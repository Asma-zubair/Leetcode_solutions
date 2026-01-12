class Solution:
    def reverse(self, x: int) -> int:
          if x < 0:
            sign=-1
          else:
            sign=1
          number=abs(x)
          rev=0

          while number != 0:
            last_digit=number%10
            rev=rev*10+last_digit
            number=number//10
            
          rev=rev*sign
          if rev < -2**31 or rev > 2**31-1:
            return 0
          return rev

                
        
