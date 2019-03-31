"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random

class Random:
  def __init__(self):
    self.last_random = None
    self.count = 0

  def set_random(self, stream):

    self.count += 1

    if self.count == 1:
      self.last_random = stream
    else:
      rand = random.randint(self.count)
      if rand == self.count - 1:
        self.last_random = stream

    return self.last_random

  def get_random(self):
    return self.last_random
