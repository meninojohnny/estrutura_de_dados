import 'node.dart';

class LinkedList {
  var head;
  int size = 0;

  LinkedList(){
    this.head = null;
  }

  void append(elem) {
    if (head) {
      Node pointer = head;
      while (pointer.next) {
        pointer = pointer.next;
      }
      pointer.next = Node(elem);
      size++;
    } else {
      head = Node(elem);
    }
  }
}