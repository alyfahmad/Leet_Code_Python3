class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx, num in enumerate(nums):
            temp_idx = idx + 1
            if temp_idx < len(nums):
                temp_value = nums[temp_idx]
                while temp_value == num:
                    nums.pop(temp_idx)
                    if temp_idx < len(nums):
                        temp_value = nums[temp_idx]
                    else:
                        break
            else:
                break

        return len(nums)

Obj = Solution()
print(Obj.removeDuplicates([1,1]))