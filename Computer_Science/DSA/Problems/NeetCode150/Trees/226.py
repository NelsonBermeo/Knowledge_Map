"""
226 - Invert Binary Tree (easy)

Given the root of a binary tree invert the tree

"""


def invertTree(root):
    if root is None:
        return None
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)
        return root
