"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def func(k, L):

  S = set([])

  for l in L:
    if l not in S:
      S.add(k-l)
    else:
      return True

  return False

print(func(17, [10, 15, 3, 7]))

