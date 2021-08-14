
#include <iostream>
#include <cstring>

using namespace std;




// Task 3.2

class ListNode {
private:
  string DataValue;
  int PointerValue;

public:
  ListNode (string data, int ptr) {
    DataValue = data;
    PointerValue = ptr;
  }

  int GetPointerValue () {
    return PointerValue;
  }

  string GetDataValue () {
    return DataValue;
  }

  void SetPointerValue (int ptr) {
    PointerValue = ptr;
  }

  void SetDataValue (string data) {
    DataValue = data;
  }

};


class LinkedList {
private:
  static ListNode Node[31];
  int Start;
  int NextFree;

public:
  LinkedList () {  // Initialise LinkedList
    Node[0] = ListNode("", 0); // Null values for Node[0] since index starts at 1, leaving this node unused.
    for (int i = 1; i < 31; i++) {
      Node[i] = ListNode("", i);
    }
    Start = 0;
    NextFree = 1;
  }

  bool IsEmpty () {return Start == 0;}

  void DisplayLinkedList () {
    std::cout << "Start: " << Start << '\n';
    std::cout << "NextFree: " << NextFree << '\n';
    std::cout << "================================" << '\n';
    std::cout << "Index | DataValue | PointerValue" << '\n';
    for (int i = 1; i < 31; i++) {
      std::cout << i << " | " << Node[i].GetDataValue() << " | " << Node[i].GetPointerValue() << '\n';
    }
  }


  // Task 3.4
};


// Task 3.1

int main() {
  int choice = 0;

  LinkedList linkedList = LinkedList();

  while (choice != 5) {
    cout << "1. Add an item" << endl;
    cout << "2. Traverse the linked list of used nodes and output the data values" << endl;
    cout << "3. Output all pointers and data values" << endl;
    cout << "5. Exit" << endl;

    cout << "Choice: " << endl;
    cin >> choice;


    // Task 3.3

    switch (choice) {
      case 1:
        //linkedList.AddNode();
        break;

      case 2:
        //linkedList.Traversal();
        break;

      case 3:
        linkedList.DisplayLinkedList();
        break;

      case 4:
        //linkedList.ReverseTraversal();
        break;

      default:
        break;
    }
  }

  return 0;
}
