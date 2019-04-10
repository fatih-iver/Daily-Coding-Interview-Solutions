"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.Next = None

class LinkedList:
  def __init__(self):
    self.root = None

  def insert(self, val):
    new = Node(val)
    new.Next = self.root
    self.root = new

  def traverse(self):
    curr = self.root
    while curr:
      print(curr.val, end=" ")
      curr = curr.Next


ll = LinkedList()

r = 1

for _ in range(10):
  r = (23*r + 17) % 11
  ll.insert(r)

ll.traverse()
 
class Smallest:
  def initialize(self, root):
    curr = root
    while curr:
      self.values.append(curr.val)
      curr = curr.Next
    self.values.sort()

  def __init__(self, root):
    self.values = []
    self.initialize(root)

  def get_kth_smallest(self, k):
    return self.values[k-1]

sma = Smallest(ll.root)  
print()
print(sma.get_kth_smallest(10))
