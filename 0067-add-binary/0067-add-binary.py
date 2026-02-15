class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        
        # Add the integers
        sum_int = a_int + b_int
        
        # Convert the sum back to a binary string
        return bin(sum_int)[2:] 