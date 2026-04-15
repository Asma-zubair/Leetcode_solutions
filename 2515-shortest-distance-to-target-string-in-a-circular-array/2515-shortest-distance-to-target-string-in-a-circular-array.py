class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        result=float('inf')
        n=len(words)

        for i in range(n):
            if words[i]==target:
                direct=abs(i-startIndex)
                circular=n-direct
                result=min(result,min(direct,circular))
        if result != float('inf'):
            return result
        else:
            return -1
