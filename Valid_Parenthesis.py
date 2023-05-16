class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        starting_brackets = ['(', '{', '[']
        if len(s) == 1:
            return False

        for char in s:
            if char in starting_brackets:
                stack.append(char)
            else:
                if len(stack) != 0 and stack[-1] == '(' and char == ')':
                    stack.pop()
                elif len(stack) != 0 and stack[-1] == '{' and char == '}':
                    stack.pop()
                elif len(stack) != 0 and stack[-1] == '[' and char == ']':
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False