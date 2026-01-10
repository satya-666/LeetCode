# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # res = []
        # def helper(node,depth):
        #     if node is None:
        #         return
        #     if depth == len(res):
        #         res.append([])
        #     res[depth].append(node.val)
        #     helper(node.left,depth+1)
        #     helper(node.right,depth+1)
        # helper(root,0)
        # return len(res)
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

