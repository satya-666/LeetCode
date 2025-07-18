# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        leaders = []
        max_val = float('-inf')
        for val in reversed(stack):
            if val >= max_val:  # allow duplicates
                leaders.append(val)
                max_val = val

        leaders.reverse()

        dummy = ListNode(0)
        curr = dummy
        for val in leaders:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

                