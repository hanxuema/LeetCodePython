# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Input: 1->2->4, 1->3->4
        # Output: 1->1->2->3->4->4
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # create empty head
        curr = dummy = ListNode(0)
        while l1 and l2: # compare 2 node, choose the smaller one
            if l1.val < l2.val:
                curr.next = l1 # append the curr node, remember curr node starts with empty value
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next # always move curr to ext node 
            
        # when l1 is 1,2,3 but l2 is 5,6,7,8,9, keep add 7,8,9, from l2
        curr.next = l1 or l2 
        
        return dummy.next
            







s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)
l2.next.next.next.next  = ListNode(6)
l2.next.next.next.next.next  = ListNode(7)
# while  l1 :
#     print(l1.val)
#     l1 = l1.next

# while  l2 :
#     print(l2.val)
#     l2 = l2.next
    
rus = s.mergeTwoLists(l1, l2)



while  rus :
    print(rus.val)
    rus = rus.next