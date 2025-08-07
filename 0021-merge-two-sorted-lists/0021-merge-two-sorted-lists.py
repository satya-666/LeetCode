# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2
        nums = []
        while curr1:
            nums.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            nums.append(curr2.val)
            curr2 = curr2.next

        nums.sort()
        if not nums :
            return None
        newhead = ListNode(nums[0])
        curr = newhead
        for val in nums[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return newhead




        
            