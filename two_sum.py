class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,val in enumerate(nums):
            temp_index = index
            for index2,val2 in enumerate(nums):
                temp_value = val
                if index2 != temp_index:
                    temp_value= temp_value + val2
                    if temp_value == target:
                        final_list = [index, index2]
                        return final_list