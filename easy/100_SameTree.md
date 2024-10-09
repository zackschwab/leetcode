# 100. Same Tree
[Link](https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used depth first search. During each iteration, I also compared each node to determine if the tree structure and values were the same. If we ever find a case where the left node is empty but the right node isn't, the trees have a different structure. We also need to return false if the values are different. 

- Time complexity O(m + n) where m = size of left tree and n = size of right tree.
- Space complexity O(1)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # If they're both empty, return true
        if not p and not q:
            return True
        
        # If one node is null and the other isn't, different tree structure
        if not p or not q:
            return False

        # Tree has same structure, but different values
        if p.val != q.val:
            return False

        # Use dfs to compare each node of the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```