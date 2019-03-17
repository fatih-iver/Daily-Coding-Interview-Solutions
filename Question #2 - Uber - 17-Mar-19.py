""" 
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
[2, 3, 6].

Follow-up: what if you can't use division?

"""

def logMult(A, lo, hi):
  if lo == hi:
    return A[lo]

  m = (hi + lo) // 2

  return logMult(A, lo, m) * logMult(A, m+1, hi)


def multWithDiv(A):

  M = 1

  for a in A:
    M *= a

  L = []

  for a in A:
    L.append(M // a)

  return L


def multNoDiv(A):

  L = []

  lo = 0
  hi = len(A) - 1

  for i in range(len(A)):
    T = A[i]
    A[i] = 1
    L.append(logMult(A, lo, hi))
    A[i] = T

  return L

print(multWithDiv([1,2,3,4,5]))
print(multNoDiv([1,2,3,4,5]))
print(logMult([1,2,3,4,5], 0, 4))