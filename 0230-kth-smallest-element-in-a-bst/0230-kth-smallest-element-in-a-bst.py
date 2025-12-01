# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        def inord(satya):
            if satya is None:
                return
            
            inord(satya.left)
            res.append(satya.val)
            inord(satya.right)
        inord(root)
        return res[k-1]