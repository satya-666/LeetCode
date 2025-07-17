# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        curr = head
        nums = []

        while curr:
            nums.append(curr.val)
            curr = curr.next

        pair_sum = [0]*(len(nums)//2)
        i , j = 0 , len(nums)-1
        while i < j:
            pair_sum[i] = nums[i] + nums[j]
            i += 1
            j -= 1
        return max(pair_sum)