class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        totalsum=0
        for num in nums:
            divisorCount=0
            divisorSum=0
            for i in range(1,int(math.sqrt(num)+1)):
                if num%i==0:
                    divisorCount+=1
                    divisorSum+=i

                    if i != num//i:
                        divisorCount+=1
                        divisorSum+=num//i

                if divisorCount > 4:
                    break
            if divisorCount == 4:
                totalsum+=divisorSum

        return totalsum
                

