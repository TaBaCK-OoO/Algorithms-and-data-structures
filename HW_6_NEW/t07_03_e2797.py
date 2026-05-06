import sys

EMPTY = -1


class ContactHashSet:
    __slots__ = ['size', 'keys', 'count']

    def __init__(self, size=300007):
        self.size = size
        self.keys = [EMPTY] * size
        self.count = 0

    def add(self, key: int):
        i = key % self.size

        while self.keys[i] != EMPTY:
            if self.keys[i] == key:
                return

            i += 1
            if i == self.size:
                i = 0

        self.keys[i] = key
        self.count += 1


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    contacts = ContactHashSet()

    for i in range(1, n + 1):
        contacts.add(int(data[i]))

    print(contacts.count)


if __name__ == '__main__':
    solve()