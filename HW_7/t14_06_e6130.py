
import sys

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self._size = 0
        self._front = None
        self._back = None

    def push_front(self, n):
        node = Node(n)
        if self._size == 0:
            self._front = self._back = node
        else:
            node.next = self._front
            self._front.prev = node
            self._front = node
        self._size += 1
        return "ok"

    def push_back(self, n):
        node = Node(n)
        if self._size == 0:
            self._front = self._back = node
        else:
            self._back.next = node
            node.prev = self._back
            self._back = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._front.item
        self._front = self._front.next
        self._size -= 1
        if self._size == 0:
            self._back = None
        else:
            self._front.prev = None
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        item = self._back.item
        self._back = self._back.prev
        self._size -= 1
        if self._size == 0:
            self._front = None
        else:
            self._back.next = None
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.item

    def back(self):
        if self._size == 0:
            return "error"
        return self._back.item

    def size(self):
        return self._size

    def clear(self):
        self._size = 0
        self._front = self._back = None
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        parts = command.split()
        method = parts[0]
        args = parts[1:]
        return getattr(self, method)(*args)


if __name__ == '__main__':
    deque = Deque()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        res = deque.execute(line)
        print(res)
        if res == "bye":
            break