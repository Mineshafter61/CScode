class Node:
  def __init__(self):
    self.__data = ''
    self.__leftPtr = -1
    self.__rightPtr = -1
  def setData(self, s):
    self.__data = s
  def setLeftPtr(self, x):
    self.__leftPtr = x
  def setRightPtr(self, y):
    self.__rightPtr = y
  def getData(self):
    return self.__data
  def getLeftPtr(self):
    return self.__leftPtr
  def getRightPtr(self):
    return self.__rightPtr
      

class Tree:
  def __init__(self):
    self.__root = -1
    self.__tree = []  # array of nodes, left as empty list since we can append later

  def compare(self, item, ptr):
    print(item.getData(), self.__tree[ptr].getData())
    if item.getData() > self.__tree[ptr].getData():
      # right hand side
      # not free
      if self.__tree[ptr].getRightPtr() != -1:
        self.compare(item, self.__tree[ptr].getRightPtr())
      # free
      else:
        self.__tree[ptr].setRightPtr(len(self.__tree)-1)
    else:
      # left hand side
      # not free
      if self.__tree[ptr].getLeftPtr() != -1:
        self.compare(item, self.__tree[ptr].getLeftPtr())
      # free
      else:
        self.__tree[ptr].setLeftPtr(len(self.__tree)-1)
      
  def add(self, newItem):
    new = Node()
    new.setData(newItem)
    self.__tree.append(new)
    # case where tree is empty
    if len(self.__tree) == 1:
      self.__root = 0

    # case of inserting at the branches
    else:
      # compare
      self.compare(new, self.__root)

  def pprint(self):  # Since print() is a Python built-in function, we cannot use that name. This is the print() function in the question.
    print("leftPtr | data | rightPtr")
    for node in self.__tree:
      print("{0:>7} |{1:^6}| {2:<8}".format(node.getLeftPtr(), node.getData(), node.getRightPtr()))

  def traverse(self, arg):
    if self.__tree[arg].getLeftPtr() != -1:
      self.traverse(self.__tree[arg].getLeftPtr())
    print(self.__tree[arg].getData())
    if self.__tree[arg].getRightPtr() != -1:
      self.traverse(self.__tree[arg].getRightPtr())

  def inOrderTraversal(self):
    self.traverse(self.__root)

t = Tree()
t.add("Dave")
t.add("Fred")
t.add("Ed")
t.add("Greg")
t.add("Bob")
t.add("Cid")
t.add("Ali")
t.pprint()
t.inOrderTraversal()
