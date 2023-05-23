class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = bin(add(int(a, 2), int(b, 2)))
        result = result[2:]

        return result