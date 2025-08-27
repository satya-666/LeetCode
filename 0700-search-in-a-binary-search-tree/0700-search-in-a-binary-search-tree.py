# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        return self.Traverse(root,val)

    def Traverse(self,root,val):
        if root is None:
            return None
        if root.val==val:
            return root
        if root.val > val:
            return self.Traverse(root.left,val)
        else:
            return self.Traverse(root.right,val)
        
        