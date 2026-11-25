"""
104 - Maximum Depth of Binary Tree
Given the root of a binary tree, return the max depth (number of nodes not edges)
"""


def maxDepth(root):
    if root is None:
        return 0
    else:
        1 + max(maxDepth(root.left), maxDepth(root.right))
