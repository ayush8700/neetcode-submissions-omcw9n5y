class Solution:
    def isValid(self, s: str) -> bool:
        paras = {"}":"{", ")":"(", "]":"["}
        stack = []
        for char in s:
            if char in paras:
                if not stack:
                    return False
                if stack.pop() != paras[char]:
                    return False
            else:
                stack.append(char)
        return not stack

        
        