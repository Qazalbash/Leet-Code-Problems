// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        d=[]
        def traversal(r,lev):
            if r:
                if len(d) < lev: d.append([r.val])
                else: d[lev-1].append(r.val)
                traversal(r.left,lev+1)
                traversal(r.right,lev+1)
        traversal(root,1)
        return d