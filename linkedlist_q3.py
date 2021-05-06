class Node:
    def __init__(self, name="empty string", pointer=-1):  # Initialise
        self.__name = str(name);
        self.__pointer = int(pointer);
		## A -1 pointer is a nullPointer

    def getName(self):
        return self.__name
    def getPointer(self):
        return self.__pointer
    def setName(self, name: str):
        self.__name = str(name);
    def setPointer(self, pointer: int):
        self.__pointer = int(pointer);
		

class LinkedList:
	def __init__(self, size=20):  # initialize
		self.__start = -1
		self.__nextfree = 0
		self.__countries = [Node() for i in range(size)]
		for i in range(len(self.__countries)-1):
			self.__countries[i].setPointer(i+1)
		
	def isEmpty(self):
		return self.__start == -1
	
	def isFull(self):
		return self.__nextfree == -1
	
	def insert(self, name):
		if self.__nextfree == -1:
			print("No free node!")
			return
		self.__countries[Nextfree].setName(name)
		if self.__start == self.__nextfree:
			self.__nextfree = self.__countries[self.__nextfree].getPointer()
			self.__countries[self.__start].setPointer(-1)
		else:
			prev = -1
			curr = self.__start
			while curr != -1:
				if name < self.__countries[curr].getName():
					break
				prev = curr
				curr = self.__countries[curr].getPointer()
			if prev == -1:
				temp = self.__start
				self.__start = self.__nextfree
				self.__nextfree = self.__countries[self.__nextfree].getPointer()
				self.__countries[self.__start].setPointer(temp)
			else:  ## store between prev and current
				self.__countries[prev].setPointer(self.__nextfree)
				self.__nextfree = self.__countries[self.__nextfree].getPointer()
				
	
	def display(self):
		for i in range(len(self.__countries):
			print('{:^4}|{:^20}|{:^4}'.format(i, self.__countries[[i].getName(), self.__countries[i].getPointer() )
		print('Start =', self.__start)
		print('Nextfree =', self.__nextfree)
	
	def traversal(self):
		current = self.__start;
		while current != -1:
			print(self.__countries[current].getName() )
			current = self.__countries[current].getPointer()
	
## Main ##
list1 = LinkedList();
list1.display();
