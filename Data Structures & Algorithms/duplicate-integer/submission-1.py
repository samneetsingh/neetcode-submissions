class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set(nums)
        if len(counter) == len(nums):
            return False
        return True