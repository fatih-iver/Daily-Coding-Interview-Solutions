""" 
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class T:
    def __init__(self):
        self.root = None
 

    def insertR(self, val, node):
        if not node:
            return Node(val)
        else:
            if random.choice([True, False]):
                node.left = self.insertR(val, node.left)
            else:
                node.right = self.insertR(val, node.right)
                
            return node
        
    def insert(self, val):
        self.root = self.insertR(val, self.root)

        
    def serializeR(self, node):
        if node:
            return str(node.val) + " " + self.serializeR(node.left) + " " + self.serializeR(node.right)
        else:
            return "#"

    def serialize(self):
        return self.serializeR(self.root)
    
    def deserializeR(self, serialized, index, max_index, node):
        if index[0] < max_index:
            if serialized[index[0]] != "#":
                val = int(serialized[index[0]])
                node = Node(val)
                index[0] += 2
                node.left = self.deserializeR(serialized, index, max_index, node.left)
                node.right = self.deserializeR(serialized, index, max_index, node.right)
                return node
            else:
                index[0] += 2
                
    
    def deserialize(self, serialized):
        self.root = None
        self.root = self.deserializeR(serialized, [0], len(serialized), self.root)
        
        

        
tree = T()
for i in range(10):
    tree.insert(i)
print(tree.serialize())

tree2 = T()
tree2.deserialize(tree.serialize())
print(tree2.serialize())
"""
Sample Serialization:
0 1 6 9 # # # 2 # 5 # # 3 7 8 # # # 4 # #
0 1 6 9 # # # 2 # 5 # # 3 7 8 # # # 4 # #
"""




