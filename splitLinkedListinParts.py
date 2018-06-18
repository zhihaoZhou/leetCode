# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]

        root = [1, 2, 3], k = 5
        Output: [[1],[2],[3],[],[]]
        """
        length = 0
        tmp = root
        while tmp:
            tmp = tmp.next
            length += 1

        avg_len, mod = length // k, length % k
        lens = [avg_len] * k
        for i in range(mod):
            lens[i] += 1
        answer = [None] * k
        tmp = root
        for i in range(k):
            answer[i] = tmp
            prev = None
            for _ in range(lens[i]):
                prev, tmp = tmp, tmp.next
            if prev:
                prev.next = None

        return answer

