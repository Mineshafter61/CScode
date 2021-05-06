class Stack:
    def __init__(self,size):
        self.__data = [None for i in range(5)]
        self.__top = -1
        self.__maxSize = 5

    def display(self):
        for i in range(len(self.__data)-1,-1,-1):
            if self.__top== i:
                print("{0:^15}{1:<10}".format(str(self.__data[i]),"<--top"))
            else:
                print("{0:^15}".format(str(self.__data[i])))

        print("-"*17)

    def isEmpty(self):
        if self.__top ==-1:
            return True
        else:
            return False

    def isFull(self):
        if self.__top == self.__maxSize-1:
            return True
        else:
            return False

    def push(self,item):
        if self.isFull():
            print("Stack is Full")
        else:
            self.__top = self.__top + 1
            self.__data[self.__top] = item

    def pop(self,item):
        if self.isEmpty():
            print("Stack is empty")
        else:
            item = self.__data[self.__top]
            self.__top = self.__top - 1
            return item
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            item = self.__data(self.__top)
            return item
