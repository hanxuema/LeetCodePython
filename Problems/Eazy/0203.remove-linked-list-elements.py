#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, dummy.next

        while cur:
            if cur.val == val:
                pre.next= cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
# @lc code=end

