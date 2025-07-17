# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        if not head or not head.next:
            return head
        curr = head
        result = []
        count = 0
        while curr:
            if curr.val == 0:
                result.append(count)
                count = 0
            else:
                count += curr.val
            curr = curr.next
        result = result[1:]
        dummy = ListNode(0)
        curr = dummy
        for val in result:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
        