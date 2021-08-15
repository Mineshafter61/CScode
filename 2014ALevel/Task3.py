class ListNode:

  def __init__(self, DataValue='', PointerValue=0):
    self.DataValue = DataValue
    self.PointerValue = PointerValue

  def setDataValue(self, DataValue):
    self.DataValue = DataValue

  def getDataValue(self):
    return self.DataValue

  def setPointerValue(self, PointerValue):
    self.PointerValue = PointerValue

  def getPointerValue(self):
    return self.PointerValue


class LinkedList:
  """Linked List obyekt."""

  def __init__(self):
    self.Node = [None] + [ListNode() for x in range(1,31)]  # インデックスが1から始まるため、最初の値をNoneとして残す
    self.Start = 0  # null 値
    self.NextFree = 1  # ンデックスが1から始める

  def DisplayLinkedList(self):
    for i in range(1, 31):
      print(i, self.Node[i].getDataValue(), self.Node[i].getPointerValue())

  def IsEmpty(self):
    return self.Start == 0

  def AddNode(self):
    NewItem = input('NewItem > ')
    self.Node[self.NextFree].setDataValue(NewItem)

    if self.Start == 0:
      self.Start = self.NextFree
      Temp = self.Node[self.NextFree].getPointerValue()
      self.Node[self.NextFree].setPointerValue(0)
      self.NextFree = Temp
    else:
      # traverse the list = starting at Start to find
      # the position at which to insert the new item
      Temp = self.Node[self.NextFree].getPointerValue()

      if NewItem < self.Node[self.Start].getDataValue():
        # new item will become the start of the List
        self.Node[self.NextFree].setPointerValue(self.Start)
        self.Start = self.NextFree
        self.NextFree = Temp
      else:
        # the new item is not at the start of the List
        Previous = 0
        Current = self.Start
        Found = False

        while not (Found == True or Current = 0):
          if NewItem <= self.Node[Current].getDataValue():
            self.Node[Previous].setPointerValue(self.NextFree)
            self.Node[self.NextFree].setPointerValue(Current)
            self.NextFree = Temp
            Found = True
          else:
            # move on to the next nodes
            Previous = Current
            Current = self.Node[Current].getPointerValue()

        if Current == 0:
          self.Node[Previous].setPointerValue(self.NextFree)
          self.Node[self.NextFree].setPointerValue(0)
          self.NextFree = Temp

  def IsFull(self):
    return self.NextFree == 0

  def TraversalInOrder(self, Index):
    if Index != 0:
      print(self.Node[Index].getDataValue())
      TraversalInOrder(self.Node[Index].getPointerValue())

  def Traversal(self):
    TraversalInOrder(self, self.Start)

  def TraversalInReverseOrder(self, Index):
    if Index != 0:
      TraversalInReverseOrder(self.Node[Index].getPointerValue())
      print(self.Node[Index].getDataValue())

  def ReverseTraversal(self):
    TraversalInReverseOrder(self, self.Start)


def main():
  ll = LinkedList()
  while True:
    # メニュー
    print('1. Add an item\n2. Traverse the linked list of used nodes and output the data values\n3. Output all pointers and data values\n4. Traverse the linked list in reverse\n5. Exit')
    choice = input('> ')
    if choice == '1':
      ll.AddNode()
    elif choice == '2':
      ll.Traversal()
    elif choice == '3':
      ll.DisplayLinkedList()
    elif choice == '4':
      ll.ReverseTraversal()
    elif choice == '5':
      break

if __name__ == '__main__':
  main()
