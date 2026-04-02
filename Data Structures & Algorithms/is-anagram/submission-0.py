class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = sorted(s)
        tList = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False
        return True
        