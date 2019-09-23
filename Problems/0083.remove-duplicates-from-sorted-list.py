#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode 1,1,2,3,3
        :rtype: ListNode     1,2,3
        """
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner =  runner.next
            current.next = runner
            current = runner
        return head


# head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3) 
# head.next.next.next.next= ListNode(3)

# print(head)
# print(Solution().deleteDuplicates(head))
