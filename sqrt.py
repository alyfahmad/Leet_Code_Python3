class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        i = 0
        while result <= x:
            i += 1
            result = i * i

        return i - 1