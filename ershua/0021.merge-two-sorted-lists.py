#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next # cur is the previous value of either l1 or l2
        cur.next = l1 or l2
        return dummy.next


# @lc code=end
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)
# print(Solution().mergeTwoLists(l1, l2))
