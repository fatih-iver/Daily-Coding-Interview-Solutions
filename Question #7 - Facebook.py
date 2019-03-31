"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
def decode(cipher):

  length = len(cipher)

  if length == 0:
    return 1
  elif length == 1:
    return decode(cipher[1:])
  else:
    f2d = int(cipher[:2])

    if f2d < 27:
      return decode(cipher[1:]) + decode(cipher[2:])
    return decode(cipher[1:])

def decode2(cipher, N, index = 0):

  if N - index == 0:
    return 1
  elif N - index == 1:
    return decode2(cipher, N, index + 1)
  else:
    f2d = int(cipher[:2])

    if f2d < 27:
      return decode2(cipher, N, index + 1) + decode2(cipher, N, index+2)
    return decode2(cipher, N, index + 1)

print(decode("111"))
print(decode2("111", 3))



