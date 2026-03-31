class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        for key,values in hashmap.items():
            if values == 1 :
                return key