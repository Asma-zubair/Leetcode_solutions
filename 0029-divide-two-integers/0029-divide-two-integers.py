class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX=2**31-1
        INT_MIN=-2**31


        if dividend == INT_MIN and divisor == -1:
            return INT_MAX


        negative=False
        if dividend < 0:
            dividend=-dividend
            negative=not negative

        if divisor < 0 :
            divisor=-divisor
            negative=not negative

        denomenator=0
        while dividend  >= divisor:
            dividend=dividend-divisor
            denomenator+=1

        if negative:
            denomenator=-denomenator
        
        return denomenator
