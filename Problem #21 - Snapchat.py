"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import heapq

def min_room(durations):

  timer = []

  for duration in durations:
    heapq.heappush(timer, (duration[0], 's'))
    heapq.heappush(timer, (duration[1], 'f'))

  min_count = 0
  curr_count = 0

  while timer:
    event = heapq.heappop(timer)
    if event[1] == 's':
      curr_count += 1
      if curr_count > min_count:
        min_count = curr_count
    else:
      curr_count -= 1

  return min_count

print(min_room([(30, 75), (0, 50), (60, 150)]))
