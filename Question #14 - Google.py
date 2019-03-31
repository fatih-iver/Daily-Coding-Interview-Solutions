"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

def estimate_pi(accuracy= 100000):

  circle_count = 0

  for _ in range(accuracy):
    if random.random()**2 + random.random()**2 <= 1:
      circle_count += 1

  return 4 * circle_count / accuracy

print(estimate_pi())
  
    
