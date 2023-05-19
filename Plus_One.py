class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if(digits[len(digits)-1] == 9):
            position = len(digits)-1
            while digits[position] == 9:
                if position == 0:
                    break
                else:
                    position -= 1 
            if digits[position] == 9:
                digits[position] = 1
                for i in range ( (position + 1), len(digits) ):
                    digits[i] = 0
                digits.append(0)
            else:
                digits[position] = digits[position] + 1
                for i in range ( (position + 1), len(digits) ):
                    digits[i] = 0

        else:
            digits[len(digits)-1] = digits[len(digits)-1] + 1

        return digits
