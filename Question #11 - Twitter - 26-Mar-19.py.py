"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class Node:
  def __init__(self, char):
    self.char = char
    self.isLeaf = False
    self.word = None
    self.children = {}

class Trie:
  def __init__(self):
    self.root = Node("")

  def insert(self, word):
    curr = self.root
  
    for char in word:
      if char not in curr.children:      
        curr.children[char] = Node(char)
      curr = curr.children[char]

    curr.isLeaf = True
    curr.word = word

  def traverseR(self, node):
    if node:
      if node.isLeaf:
        print(node.word)

      for child in node.children:
        self.traverseR(node.children[child])

  def getRef(self, prefix):
    curr = self.root
    for char in prefix:
      if char not in curr.children:
        return None # No such string exist
      else:
        curr = curr.children[char]

    return curr

  def find(self, prefix):
    node = self.getRef(prefix)
    if node:
      self.traverseR(node)
    else:
      print("No Suggestion")

  def traverse(self):
    self.traverseR(self.root)

T = Trie()

T.insert("fatih")
T.insert("fatma")
T.insert("serkan")
T.insert("semih")
T.insert("yasin")
T.insert("nergul")
T.insert("nergiz")
T.insert("furkan")

T.traverse()

print()
T.find("se")
print()
T.find("fat")
print()
T.find("f")
print()
T.find("ne")
print()
T.find("")
