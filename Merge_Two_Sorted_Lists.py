# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Definition for singly-linked list.
        # class ListNode(object):
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution(object):
            def mergeTwoLists(self, l1, l2):
                """
                :type list1: Optional[ListNode]
                :type list2: Optional[ListNode]
                :rtype: Optional[ListNode]
                """
                # if not list1 or not list2:
                # return list1 or list2
                # if list1.val < list2.val:
                #     list1.next = self.mergeTwoLists(list1.next, list2)
                #     return list1
                # else:
                #     list2.next = self.mergeTwoLists(list1, list2.next)
                #     return list2

                counter = 0
                dummy = cur = ListNode(0)
                while l1 and l2:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                    print(counter)
                    print(cur)
                    counter += 1
                    cur = cur.next
                cur.next = l1 or l2
                return dummy.next



Obj = Solution()
print(Obj.mergeTwoLists([],[]))