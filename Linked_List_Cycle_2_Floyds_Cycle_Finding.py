# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            print('cycle check')
            print(str(tortoise.val) + ' & ' + str(hare.val))

            if tortoise == hare:
                tortoise = head
                while tortoise != hare:
                    print('cycle index')
                    print(str(tortoise.val) + ' & ' + str(hare.val))
                    tortoise = tortoise.next
                    hare = hare.next
                return tortoise

        return None