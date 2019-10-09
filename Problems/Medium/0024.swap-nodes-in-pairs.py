#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next= head
        pre = dummy
        while pre.next and pre.next.next:
            preNext= pre.next
            preNextNext = preNext.next

            pre.next, preNextNext.next, preNext.next = preNextNext, preNext, preNextNext.next

            pre = preNext

        return dummy.next

    def printNode(self, nodeName, node):
        print(nodeName+"  ", end = '')
        while node:
            print("{}-->".format(node.val), end = '')
            node = node.next
        print("")
    def convertToNode(self, arr):
        head= ListNode(-1)
        cur = head
        for v in arr:
            cur.next =ListNode(v)
            cur = cur.next
        return head.next

s = Solution()
n = s.convertToNode([1,2,3,4,5])
s.printNode("head",n)
s.printNode("res ",s.swapPairs(n))
# @lc code=end

