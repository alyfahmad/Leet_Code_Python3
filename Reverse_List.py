# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = cur = ListNode(0)
        flag = True

        while head != None:
            if flag:
                temp = ListNode(head.val)
                cur.next = temp
                cur = dummy
                head = head.next
                flag = False
            else:
                prev_next = cur.next
                temp = ListNode(head.val)
                cur.next = temp
                cur.next.next = prev_next
                cur = dummy
                head = head.next

        return dummy.next