# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        total_nodes = 1
        while dummy.next is not None:
            dummy = dummy.next
            total_nodes += 1

        middle_node = total_nodes/2 + 1
        splitter_count = 1

        while head.next is not None:
            if splitter_count == middle_node:
                break
            else:
                head = head.next
                splitter_count += 1

        return head