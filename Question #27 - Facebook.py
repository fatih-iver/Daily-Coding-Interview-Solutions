"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def isbalanced(parantheses):
    
  stack = []

  for paranthesis in parantheses:

    if paranthesis in ("(", "{", "["):
      stack.append(paranthesis)

    else:
      if stack:
        prev_paranthesis = stack.pop()

        if paranthesis == ")":
          if prev_paranthesis != "(":
            return False
          continue

        if paranthesis == "}":
          if prev_paranthesis != "{":
            return False
          continue

        if paranthesis == "]":
          if prev_paranthesis != "[":
            return False
          continue

      else:
        return False

  return False if stack else True

print(isbalanced("([])[]({})"))
print(isbalanced("([)]"))
print(isbalanced("((()"))
