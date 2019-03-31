"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

import uuid

class Order:
  def __init__(self):
    self.ID = uuid.uuid4()

class Server:
  def __init__(self, N):
    self.N = N
    self.curr_index = 0
    self.last_N_orders = [0 for _ in range(N)]

  def record(self, order_id):
    self.last_N_orders[self.curr_index % self.N] = order_id
    self.curr_index += 1

  def get_last(self, index):
    return self.last_N_orders[(self.curr_index - index + self.N) % self.N]

server = Server(5)

for _ in range(7):
  ID = uuid.uuid4()
  print(str(ID)[:6], end=" ")
  server.record(str(ID)[:6])
print()
for i in range(1,6):
  print(server.get_last(i))

  


