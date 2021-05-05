NullPointer = -1
class TreeNode:
  def __init__(self, data, lptr=0, rptr=0):
    self.__data = data
    self.__lptr = lptr
    self.__rptr = rptr

  def getdata():
    return self.__data
  def getlptr():
    return self.__lptr
  def getrptr():
    return self.__rptr
  def setdata(data):
    self.__data = data
  def setlptr(lptr):
    self.__lptr = lptr
  def setrptr(rptr):
    self.__rptr = rptr

class BST:
  def __init__(self, size):
    self.__Tree = [None] + [TreeNode('') for i in range(size)]

    for i in range(1, len(self.__Tree)):
      self.__Tree[i].setlptr(i)

    self.__Tree[len(self.__Tree) - 1].setlptr(NullPointer)
    self.__RootPointer = NullPointer

    self.__FreePtr = 1

  def insert(self, Newitem):
    if self.__FreePtr != NullPointer:
      NewNodePtr = self.__FreePtr
      self.__FreePtr = self.__Tree[self.__FreePtr].getlptr()
      self.__Tree[newNodePtr]

  def find(self, Searchitem):
    cur = RootPointer
    while cur != NullPointer and (self.__Tree[cur].getdata() != Searchitem):
      if Searchitem < self.__Tree[cur].getdata():
        cur = self.__Tree[cur].getlptr()
      else:
        cur = self.__Tree[cur].getlptr()
    return cur

  def inorder(self, index):
    if index != NullPointer:
      self.inorder(self.__Tree[index].getlptr())
      print(self.__Tree[index].getdata)
      self.inorder(self.__Tree[index].getrptr())

  def preorder(self, index):
    if index != NullPointer:
      print(self.__Tree[index].getdata)
      self.preorder(self.__Tree[index].getlptr())
      self.preorder(self.__Tree[index].getrptr())

  def postorder(self, index):
    if index != NullPointer:
      self.postorder(self.__Tree[index].getlptr())
      self.postorder(self.__Tree[index].getrptr())
      print(self.__Tree[index].getdata)

def main():
    bst = BST(10)
    ## bst.display()
    bst.InsertNode("Mango")
    bst.InsertNode("Papaya")
    bst.InsertNode("Banana")
    bst.InsertNode("Rambutan")
    bst.InsertNode("Apple")
    bst.InsertNode("Avocado")
    bst.display()
    print(bst.FindNode("Apple"))
main()
