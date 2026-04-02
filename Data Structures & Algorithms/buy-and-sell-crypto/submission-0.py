class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPr = 0
        currPr = 0
        left = prices[0]

        for right in prices[1:]:
            currPr = right - left
            if currPr < 0:
                left = right
            maxPr = max(maxPr, currPr)
        return maxPr
        