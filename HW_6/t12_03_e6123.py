import sys


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item: int) -> str:
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"

        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self._size == 0:
            return "error"
        return self._top.item

    def size(self) -> int:
        return self._size

    def clear(self) -> str:
        self._top = None
        self._size = 0
        return "ok"

    def exit(self) -> str:
        return "bye"


if __name__ == "__main__":
    stack = Stack()

    for line in sys.stdin:
        command = line.split()
        if not command:
            continue

        method = command[0]
        if method == "push":
            print(stack.push(int(command[1])))
        elif method == "pop":
            print(stack.pop())
        elif method == "back":
            print(stack.back())
        elif method == "size":
            print(stack.size())
        elif method == "clear":
            print(stack.clear())
        elif method == "exit":
            print(stack.exit())
            break