class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        primary_string = strs[0]
        prefix = ""

        for char in primary_string:
            for i in range(1, len(strs)):
                if strs[i].startswith(prefix + char) is False:
                    return prefix
            prefix += char

        return prefix