class ConnectionNode:
    def __init__(self, DataValue='', LeftChild=0, RightChild=0):
        self.__DataValue = DataValue
        self.__LeftChild = LeftChild
        self.__RightChild = RightChild

    def getDataValue(self):
        return self.__DataValue

    def getLeftChild(self):
        return self.__LeftChild

    def getRightChild(self):
        return self.__RightChild

    def setDataValue(self, DataValue):
        self.__DataValue = DataValue

    def setLeftChild(self, LeftChild):
        self.__LeftChild = LeftChild

    def setRightChild(self, RightChild):
        self.__RightChild = RightChild

class LinkedList:
    def __init__(self, size=25):
        self.__RobotData = [None]+[ConnectionNode() for i in range(size)]  # py indexing starts from 0, so we leave index 0 out as a None object
        self.__Root = 0
        self.__NextFreeChild = 1

        for i in range(1, size):  # don't do this for last node
            self.__RobotData[i].setLeftChild((i+1))

ll = LinkedList()
# ll._LinkedList__RobotData.remove(None)
# for node in ll._LinkedList__RobotData:
#     print(node._ConnectionNode__DataValue)
#     print(node._ConnectionNode__LeftChild)
#     print(node._ConnectionNode__RightChild)