# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        result_dict = {}
        while curr :
            if curr.val in result_dict:
                result_dict[curr.val] += 1
            else:
                result_dict[curr.val] = 1 
            curr = curr.next

        arr = []
        # for key,value in result_dict.items():
        #     if value == 1:
        #         arr.append(key)
        arr = [key for key, value in result_dict.items() if value == 1]
        arr.sort()
        if not arr: 
            return None
        newnode = ListNode(arr[0])
        curr = newnode
        for val in arr[1:]:
            curr.next = ListNode(val)  
            curr = curr.next  
        return newnode