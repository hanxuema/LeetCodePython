#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry 
            cur.next = ListNode(sum % 10)
            carry = sum // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        left = l1 or l2 # l1 1,2  l2 3,5,7
        while left:
            sum = left.val + carry
            cur.next = ListNode(sum % 10)
            carry = sum // 10
            left = left.next
            cur = cur.next
        
        if carry == 1: #l1 1,2 l2 9,9,9
            cur.next = ListNode(1)

        return dummy.next

# @lc code=end

