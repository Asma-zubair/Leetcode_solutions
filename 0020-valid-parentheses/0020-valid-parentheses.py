class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        validset={")":"(", "}":"{","]":"["}
        for c in s:
            if c in validset:
                if stack and stack[-1]==validset[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0