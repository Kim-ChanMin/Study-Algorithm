'''
LeetCode 26. Remove Duplicates from Sorted Array
Language : Python
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        idx = 0

        for num in range(1, len(nums)):
            if nums[idx] != nums[num]:
                idx += 1
                nums[idx] = nums[num]

        return idx + 1
