# Linked List
class Node:
  def __init__(self, data, ptr=-1):
    self.__data = data;
    self.__ptr  = ptr;

  def setdata(self, data):
    self.__data = data;

  def setptr(self, ptr):
    self.__ptr  = ptr;

  def getdata(self):
    return self.__data

  def getptr(self):
    return self.__ptr

class LinkedList(object):
  """Linked List: makes a linked list of memory 128"""
  def __init__(self, size = 128):
    self.__list = [Node(None) for i in range(size)]
    for i in range(len(self.__list)):
      if i != len(self.__list)-1:
        self.__list[i].setptr(i+1)
    self.__start = -1;
    self.__free  = 0;

  def insert(self, data):
    if self.__free == -1:
      print("Error: Linked List full!")
      return False
    else:
      self.__list[self.__free].setdata(data)
      if self.__start == -1:
        # Case 1: empty list
        temp = self.__list[self.__free].getptr()
        self.__list[self.__free].setptr(-1)
        self.__start = self.__free
        self.__free = temp
      else:
        prev = -1
        curr = self.__start
        # Traverse
        while curr != -1 and not data < self.__list[curr].getdata():
          prev = curr
          curr = self.__list[curr].getptr()
        temp = self.__list[self.__free].getptr()
        self.__list[self.__free].setptr(curr)
        # Case 2: 1st element
        if prev == -1:
          self.__start = self.__free
        # Case 3: middle element
        else:
          self.__list[prev].setptr(self.__free)
        self.__free = temp

  def delete(self, data):
    if self.__start == -1:
      print("Error: Linked List empty!")
      return False
    else:
      prev = -1
      curr = self.__start
      while curr != -1 and not data == self.__list[curr].getdata():
        prev = curr
        curr = self.__list[curr].getptr()
      temp = self.__list[curr].getptr()
      self.__list[curr].setptr(self.__free)
      self.__free = curr
      if prev == -1:
        # Case 1: 1st element
        self.__start = temp
      else:
        # Case 2: middle element
        self.__list[prev].setptr(temp)

  def display(self):
    print(self.__start, self.__free)
    j=0
    for i in self.__list:
      print(j, i.getdata(), i.getptr())
      j+=1

class Queue(LinkedList):
  """docstring for Queue."""
  def __init__(self, arg):
    super(Queue, self).__init__()
    self.arg = arg


def quicksort(arr):
  lo=0; hi=len(arr);
  if len(arr) == 1:
    return arr
  else:
    pivot = arr[-1]
    pivotindex = hi-1
    i = lo
    while i < hi:
      if arr[i] > pivot:
        temp = arr[i]
        for j in range(i+1, pivotindex):
          arr[j-1] = arr[j]
        pivotindex -= 1
      else:
        i += 1
    return quicksort(arr[lo:pivotindex])+quicksort(arr[pivotindex+1:hi])


if __name__ == '__main__':
  l = LinkedList(4)
  l.insert('stupid'); l.insert('piece'); l.insert('of'); l.insert('shit'); l.display(); l.delete('stupid'); l.display(); l.delete('of'); l.display();
  print(quicksort([2,4,3,6,8,5]))
