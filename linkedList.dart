import 'node.dart';

class LinkedList {
  var head = null;
  int __size = 0;

  LinkedList();

  void append(elem) {

    if (__size > 0) {

      Node pointer = head;
      while (pointer.next) {
        pointer = pointer.next;
      }
      pointer.next = Node(elem);
      __size++;

    } else {
      __size++;
      head = Node(elem);

    }
  }

  int len() {
    return __size;
  }

  get(index) {
    Node pointer = head;
    for (int i = 0;i != index;i++) {
      pointer = pointer.next;
    }
    print(pointer.data);

  }

}