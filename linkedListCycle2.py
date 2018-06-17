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

        cycle_len = 0
        while True:
            slow = slow.next
            fast = fast.next.next
            cycle_len += 1
            if slow == fast:
                break

        r1 = r2 = head
        # position r2 cycle_len units ahead of r1
        for i in range(cycle_len):
            r2 = r2.next
        while r1 != r2:
            r1 = r1.next
            r2 = r2.next
        return r1




