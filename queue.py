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

class Queue:
    def __init__(self, limit=None):
        if limit==None:
            self.__limit = int(input("How many nodes in total? : "))
        else:
            self.__limit = limit
        self.__queue = [Node("") for i in range(self.__limit)]
        for i in range(self.__limit-1):
            self.__queue[i].setptr(i+1)
        self.__front = -1  # use -1 as null
        self.__size  = 0
        self.__freelisthead = 0  # initialsie first free node to 0

    def display(self):
        for i in range(self.__limit):
            print("{:^5}|{:^21}|{:^5}".format(i, self.__queue[i].getdata(), self.__queue[i].getptr()))
        print("Front pointer:", self.__front)
        print("Freelisthead :", self.__freelisthead)
        print("Limit        :", self.__limit)
        print("Current size :", self.__size)
        
    def enqueue(self, data):
        if self.__freelisthead == -1:
            return "Queue overflow"
        p = self.__front
        while self.__queue[p].getptr() != -1:
            p = self.__queue[p].getptr()
        self.__queue[self.__freelisthead].setdata(data)
        temp = self.__queue[self.__freelisthead].getptr()
        self.__queue[self.__freelisthead].setptr(-1)
        if self.__front == -1:
            self.__front = self.__freelisthead
        else:
            self.__queue[p].setptr(self.__freelisthead)
        self.__freelisthead = temp

    def dequeue(self):
        if self.__front == -1:
            return "Queue underflow"
        dq = self.__queue[self.__front].getdata()
        temp = self.__front
        self.__front = self.__queue[self.__front].getptr()
        self.__queue[temp].setptr(self.__freelisthead)
        self.__freelisthead = temp

    def __add__(self, data):
        self.enqueue(data)

    def __sub__(self, data):
        self.dequeue()

