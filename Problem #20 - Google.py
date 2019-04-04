"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.root = None
    self.length = 0

  def insert(self, val):
    self.length += 1
    if self.root:
      new_node = Node(val)
      new_node.next = self.root.next
      self.root.next = new_node
    else:
      self.root = Node(val)

  def traverse(self):
    curr = self.root
    while curr:
      print(curr.val, end = " ")
      curr = curr.next

class Intersect:
  def __init__(self, ll1, ll2):
    self.ll1 = ll1
    self.ll2 = ll2

  def move_n_unit(self, curr, n):

    while n > 0:
      n -= 1
      curr = curr.next

  def find_intersection(self):
      curr1 = ll1.root
      curr2 = ll2.root

      diff = abs(ll1.length - ll2.length)

      if ll1.length > ll2.length:
        self.move_n_unit(curr1, diff)
      else:
        self.move_n_unit(curr2, diff)

      while curr1:
        if curr1.val == curr2.val:
          return curr1.val
        else:
          curr1 = curr1.next
          curr2 = curr2.next



ll1 = LinkedList()
ll1.insert(3)
ll1.insert(10)
ll1.insert(8)
ll1.insert(7)
ll1.traverse()

print()

ll2 = LinkedList()
ll2.insert(99)
ll2.insert(10)
ll2.insert(8)
ll2.insert(1)
ll2.traverse()

intrsct = Intersect(ll1, ll2)

print()
print(intrsct.find_intersection())
