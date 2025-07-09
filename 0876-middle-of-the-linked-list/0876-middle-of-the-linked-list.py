# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        current = head
        for i in range(count//2):
            current = current.next
        return current
            
