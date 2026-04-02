class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] *len(nums)
        suffix = [1] *len(nums)
        n= len(nums)
        prefix[1] = nums[0]
        for i in range(2, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix[n-2] = nums[n-1]
        for i in range(n-3, -1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            nums[i] = prefix[i] * suffix[i]
        return nums



        