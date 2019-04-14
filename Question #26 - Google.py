 """
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

def remove_kth(ll, k):

  if k < 1:
    return False

  curr = ll.root

  while curr and k > 0:
    curr = curr.next
    k -= 1

  if curr:
    prev = ll.root
    while curr.next:
      prev = prev.next
      curr = curr.next
    prev.next = prev.next.next
  else:
    if k == 0:
      ll.root = ll.root.next
    else:
      return False
    
  return True
