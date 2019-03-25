""" 
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

def unival(node):
  if node:
    left_count, is_left_unival = unival(node.left)
    right_count, is_right_unival = unival(node.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
      if node.left != None and node.val != node.left.val:
        return total_count, False
      elif node.right != None and node.val != node.right.val:
        return total_count, False
      else:
        return total_count+1, True
  return 0, True