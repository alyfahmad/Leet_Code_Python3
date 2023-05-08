# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = ''
        string2 = ''
        cur_node = l1.head
        while cur_node != None:
            string1 = string1 + cur_node.val
            cur_node = cur_node.next
        cur_node = l2.head
        while cur_node != None:
            string2 = string2 + cur_node.val
            cur_node = cur_node.next
        reversed_string1 = string1[::-1]
        reversed_string2 = string2[::-1]
        sum_val = int(reversed_string1) + int(reversed_string2)
        sum_val_string = str(sum_val)
        l3 = ListNode()
        cur_node = l3.head
        for i in sum_val_string:
            cur_node.val = i
            cur_node = cur_node.next
        return l3






