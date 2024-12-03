from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.preorderTraversalRec(root, res)
    
    def preorderTraversalRec(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if not root:
            return res
        else:
            res.append(root.val)
            self.preorderTraversalRec(root.left, res)
            self.preorderTraversalRec(root.right, res)

            return res
