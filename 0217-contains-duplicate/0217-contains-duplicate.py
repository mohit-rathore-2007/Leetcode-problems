class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = set()
        for i in nums:
            if i in result:
                return True

            else:
                result.add(i)
        return False
            

            

            