class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = dict()
        for i in range(len(nums)):
            if nums[i] in numsDict:
                return True
            else:
                numsDict[nums[i]] = 1
        return False
