class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while nums.index(val) != -1:
                nums.remove(val)
        except ValueError:
            return len(nums)


Obj = Solution()
print(Obj.removeElement([0,1,2,2,3,0,4,2], 2))
