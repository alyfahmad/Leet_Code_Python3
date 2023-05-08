class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        for idx in s:
            list1.append(s.index(idx))
        for idx in t:
            list2.append(t.index(idx))
        if list1 == list2:
            return True
        return False



Obj = Solution()
print(Obj.isIsomorphic("egg","add"))