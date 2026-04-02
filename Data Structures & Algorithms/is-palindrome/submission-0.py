class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(cleanS)//2):
            if cleanS[i] != cleanS[len(cleanS)-i-1]:
                return False
        return True