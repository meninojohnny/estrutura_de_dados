class Pilha {
  List items = [];
  Pilha();

  bool isEmpty() {
  return this.items == [];
  }

  void push(item) {
    items.add(item);
  }

  void pop() {
  print(items.removeLast());
  }

  int peek() {
    return items[items.length - 1];
  }

  int size() {
    return items.length;
  }

}