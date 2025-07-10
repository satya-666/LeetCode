# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        result = ''
        curr = head
        while curr:
            result += str(curr.val)
            curr = curr.next
        return int(result, 2)
