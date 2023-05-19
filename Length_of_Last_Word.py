class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_length = len(s) - 1
        space_flag = False
        length = 0
        for i in range (0, string_length):
            if s[string_length] != ' ':
                space_flag = True
                length += 1
                string_length -= 1
            elif s[string_length] == ' '  and space_flag ==  True:
                break
            else:
                string_length -= 1

        return length
