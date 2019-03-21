"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def stripe(L):
    
    M = max(L)
    
    lo = 0
    hi = len(L) - 1
    
    # seperate positives and negatives
    while True:
        
        while lo < hi and L[lo] > 0:
            lo += 1
            
        while hi > lo and 0 >= L[hi]:
            hi -= 1
            
        if lo < hi:
            L[lo], L[hi] = L[hi], L[lo]
        else:
            break
    
    # mark indexes for positives 
    for i in range(lo):
        ci = abs(L[i])-1
        if ci < lo:
            L[ci] = -abs(L[ci])
    
    # find first unmarked index
    for i in range(lo):
        if L[i] > 0:
            return i+1
        
    # if all positives marked then
    return M+1

    
print(stripe([3, 4, -1, 1]))
print(stripe([1, 2, 0]))
print(stripe([-1,3,3,5,6,3,-3,-6,-7,3,-2,5,60,-1,-1,0]))