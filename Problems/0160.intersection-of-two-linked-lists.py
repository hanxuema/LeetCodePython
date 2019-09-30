#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p2
        
# @lc code=end

