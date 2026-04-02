class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i in range(len(nums)):
            num2 = target-nums[i]
            if num2 in HashMap:
                return [HashMap[num2], i]
            else:
                HashMap[nums[i]] = i
            
        