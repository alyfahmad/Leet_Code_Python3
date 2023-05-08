class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # average: float = 0.0
        # for sl in salary:
        #     if sl != max(salary) and sl != min(salary):
        #         average += sl
        #
        # average = average/(len(salary)-2)

        salary.sort()
        average: float = 0.0
        average = (sum(salary) - salary[0] - salary[len(salary) - 1]) / (len(salary) - 2)

        return average


Obj = Solution()
print(Obj.average([1000, 2000, 3000]))
