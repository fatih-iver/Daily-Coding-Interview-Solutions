import time

def schedule(func, n_seconds):
  time.sleep(n_seconds*1000)
  return func()
