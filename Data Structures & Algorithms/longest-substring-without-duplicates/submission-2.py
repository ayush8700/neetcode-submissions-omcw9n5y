class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        chars = {}
        left = 0
        for i in range(len(s)):
            if s[i] in chars and left < chars[s[i]]+1:
                left = chars[s[i]]+1
            chars[s[i]] = i
            maxLen = max(maxLen, i-left +1)

        return maxLen


        