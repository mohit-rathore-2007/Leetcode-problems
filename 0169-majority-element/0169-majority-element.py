class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if not nums:
            return None
        nums.sort()
        n = len(nums)
        return nums[n//2]