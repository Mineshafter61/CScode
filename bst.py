NullPointer = 0;

class TreeNode:
    def __init__(self, data, left = 0, right=0):
        self.__Data = data
        self.__LeftPointer = left
        self.__RightPointer = right
    def getData(self):
        return self.__Data
    def getLeftPtr(self):
        return self.__LeftPointer
    def getRightPtr(self):
        return self.__RightPointer
    def setData(self, data):
        self.__Data = data
    def setLeftPtr(self, left):
        self.__LeftPointer = left
    def setRightPtr(self, right):
        self.__RightPointer = right

class BST:
    def __init__(self, size = 7):
        self.__Tree = [None] + [TreeNode('') for i in range(7)] # ignore index 0 by setting a dummy
        for i in range(1, len(self.__Tree) ):
            self.__Tree[i].setLeftPtr(i+1)
        self.__Tree[len(self.__Tree)-1].setLeftPtr(NullPointer)
        self.__RootPointer = NullPointer  # empty BST
        self.__FreePtr = 1                # first free node is at index 1

    def display(self):
        for i in range(1, len(self.__Tree)):
            print(i, self.__Tree[i].getLeftPtr(), self.__Tree[i].getData(), self.__Tree[i].getRightPtr())

    def insert(self, newitem):
        if self.__FreePtr != NullPointer:
            NewNodePtr = self.__FreePtr
            self.__FreePtr = self.__Tree[self.__FreePtr].getLeftPtr()
            self.__Tree[NewNodePtr].setData(newitem)
            self.__Tree[NewNodePtr].setLeftPtr(NullPointer)
            self.__Tree[NewNodePtr].setRightPtr(NullPointer)

            if self.__RootPointer == NullPointer:
                self.__RootPointer = NewNodePtr
            else:
                cur = self.__RootPointer
                while cur != NullPointer:
                    prev=cur
                    if newitem < self.__Tree[cur].getData():
                        TurnedLeft = True
                        cur = self.__Tree[cur].getLeftPtr()
                    else:
                        TurnedLeft = False
                        cur = self.__Tree[cur].getRightPtr()
                if TurnedLeft == True:
                    self.__Tree[prev].setLeftPtr(NewNodePtr)
                else:
                    self.__Tree[prev].setRightPtr(NewNodePtr)
def main():
    bst = BST()
    
    bst.insert(1)
    bst.insert(2)
    bst.display()

main()
