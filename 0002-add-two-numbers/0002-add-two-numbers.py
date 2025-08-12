# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2

        re1 = ''
        re2 = ''

        while curr1:
            re1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            re2 += str(curr2.val)
            curr2 = curr2.next

        re1 = int(re1[::-1])
        re2 = int(re2[::-1])

        total = re1 + re2
        digits = list(map(int, str(total)[::-1]))

        dummy = ListNode()
        curr = dummy
        for d in digits:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next