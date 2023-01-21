// https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        d = []
        def trav(r,lev):
            if r:
                if len(d)<lev: d.append([r.val])
                else: d[lev-1].append(r.val)
                trav(r.left,lev+1)
                trav(r.right,lev+1)
        trav(root,1)
        avg=lambda lst: sum(lst)/len(lst)
        return [avg(i) for i in d]