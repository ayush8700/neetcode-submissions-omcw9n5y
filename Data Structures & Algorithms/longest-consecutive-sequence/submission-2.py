class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        current = 0
        numSet = set(nums)
        counts = 0
        for num in numSet:
            if num-1 not in numSet:
                counts = 0
                current = num
            while current in numSet:
                counts += 1
                current += 1
            maxCount = max(maxCount, counts)
        return maxCount