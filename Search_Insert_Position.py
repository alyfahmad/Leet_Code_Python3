class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position = 0
        try:
            if nums.index(target) != -1:
                position = nums.index(target)
        except ValueError:
            for idx, num in enumerate(nums):
                if idx == (len(nums) - 1):
                    if nums[idx] < target:
                        position = idx + 1
                    else:
                        position = idx
                elif num > target:
                    position = idx
                    break

        return position