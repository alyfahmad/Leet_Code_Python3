class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for num in range(0, len(nums)):
        #     left_value: int = 0
        #     right_value: int = 0
        #     temp_pos = num
        #     for num2 in range(0, num):
        #         left_value += nums[num2]
        #     for num3 in range(num + 1, len(nums)):
        #         right_value += nums[num3]
        #
        #     if left_value == right_value:
        #         return num
        #     elif num == len(nums)-1:
        #         return -1

        left_value, right_value = 0, sum(nums)

        for idx, num in enumerate(nums):
            right_value -= num

            if left_value == right_value:
                return idx
            else:
                left_value += num

        return -1


Obj = Solution()
print(Obj.pivotIndex([2,1,-1]))
