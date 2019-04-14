"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def getlines(words, k):

  line = []
  lines = []
  line_length = 0

  for word in words:
    line.append(word)
    line_length += len(word)

    if line_length < k:
      line_length += 1
    elif line_length == k:
      lines.append(line)
      line = []
      line_length = 0
    else:
      extra_word = line.pop()
      lines.append(line)
      line = [extra_word]
      line_length = len(extra_word) + 1
  
  if line:
    lines.append(line)

  return lines

def justify_lines(lines, k):

  lines_m = []

  for line in lines:

    interval_num = len(line) - 1

    line_length = 0

    for word in line:
      line_length += len(word)

    needed_char = k - line_length

    if interval_num == 0:
      lines.append(line[0] + " " * needed_char)
    else:
      base_space = needed_char // interval_num
      extra_space = needed_char % interval_num

      spaces = [base_space for _ in range(interval_num)]

      for index in range(extra_space):
        if index % 2 == 0:
          spaces[index] += 1
        else:
          spaces[-index] += 1

      spaces.append(0)

      line_builded = ""

      for word, space_number in zip(line, spaces):
        line_builded += word + " " * space_number 

      lines_m.append(line_builded)

  return lines_m

def justify(words, k):
  lines = getlines(words, k)
  return justify_lines(lines, k)

justified_lines = justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "colour"], 16)

for justified_line in justified_lines:
  print(justified_line)

"""
Output:
>> the  quick brown
   fox  jumps  over
   the   lazy   dog
   colour
"""
