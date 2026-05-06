import sys


class Node:
    __slots__ = ['value', 'next_node']

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Queue:
    __slots__ = ['head', 'tail', 'count']

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.count += 1
        return "ok"

    def pop(self):
        if self.is_empty():
            return "error"

        val = self.head.value
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None

        self.count -= 1
        return val

    def get_front(self):
        if self.is_empty():
            return "error"
        return self.head.value

    def get_size(self):
        return self.count

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
        return "ok"


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    queue = Queue()
    i = 0
    n = len(data)

    while i < n:
        cmd = data[i]
        i += 1

        if cmd == "exit":
            print("bye")
            break
        elif cmd == "push":
            print(queue.push(data[i]))
            i += 1
        elif cmd == "pop":
            print(queue.pop())
        elif cmd == "front":
            print(queue.get_front())
        elif cmd == "size":
            print(queue.get_size())
        elif cmd == "clear":
            print(queue.clear())


if __name__ == '__main__':
    solve()