# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        count = 0 
        while curr:
            count += 1
            curr = curr.next
        kim = count-n
        current = head
        if n == count:
            head = head.next
            return head
        current = head
        for i in range(kim-1):
            current = current.next
        current.next = current.next.next
        return head
            
        