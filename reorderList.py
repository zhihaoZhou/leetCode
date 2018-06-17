# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # cut the arr in halves and return them
        def cut_arr(start, end):  # end exclusive
            slow = fast = start
            slow_prev = None
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow_prev = slow
                slow = slow.next
            # slow is now the mid
            slow_prev.next = None
            return start, slow

        def reverse_arr(head):
            cur, prev = head, None
            while cur:
                cur.next, cur, prev = prev, cur.next, cur
            return prev

        l, r = cut_arr(head, None)
        r = reverse_arr(r)
        # reorder
        while l:
            l.next, l = r, l.next
            if l:
                r.next, r = l, r.next



