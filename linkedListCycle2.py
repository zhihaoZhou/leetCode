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
        if not head:
            return None

        is_cycle = False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break  # meet for the 1st time
        if not is_cycle:
            return None

        slow = head
        # now only move fast one step each time
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast




