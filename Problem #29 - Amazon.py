"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def encode(decoded):

  if decoded and len(decoded) > 0:

    prev_char = decoded[0]
    encoded = []

    count = 0

    for index in range(len(decoded)):
      curr_char = decoded[index]
      if prev_char != curr_char:
        encoded.append(str(count))
        encoded.append(prev_char)
        prev_char = curr_char
        count = 1
      else:
        count += 1
    else:
      encoded.append(str(count))
      encoded.append(prev_char)

    return "".join(encoded)
  return ""

print(encode("AAAABBBCCDAA"))
print(encode("BAAAAAB"))


def decode(encoded):

  start = 0
  decoded = []

  for index in range(len(encoded)):
    character = encoded[index]
    if character.isalpha():
      num_repetition = int(encoded[start:index])
      start = index + 1
      decoded.append(character * num_repetition)

  return "".join(decoded)

print(decode("4A3B2C1D2A"))
print(decode("1D5A1B1C"))


