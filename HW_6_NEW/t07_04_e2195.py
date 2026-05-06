import sys

EMPTY = ""


class VocabularyHashTable:
    __slots__ = ['size', 'keys', 'used', 'count']
    M = 31

    def __init__(self, size=2003):
        self.size = size
        self.keys = [EMPTY] * size
        self.used = [False] * size
        self.count = 0

    def hash(self, key: str):
        h = 0
        for char in key:
            h = (h * self.M + ord(char)) % self.size
        return h

    def add(self, key: str):
        i = self.hash(key)
        while self.keys[i] != EMPTY:
            if self.keys[i] == key:
                return
            i += 1
            if i == self.size:
                i = 0

        self.keys[i] = key
        self.count += 1

    def mark_used(self, key: str) -> bool:
        i = self.hash(key)
        while self.keys[i] != EMPTY:
            if self.keys[i] == key:
                self.used[i] = True
                return True
            i += 1
            if i == self.size:
                i = 0
        return False

    def all_used(self) -> bool:
        for i in range(self.size):
            if self.keys[i] != EMPTY and not self.used[i]:
                return False
        return True


def solve():
    data = sys.stdin.read()
    if not data:
        return

    lines = data.splitlines()
    if not lines:
        return

    first_line_parts = lines[0].split()
    n = int(first_line_parts[0])
    m = int(first_line_parts[1])

    vocabulary = VocabularyHashTable()

    for i in range(1, n + 1):
        word = lines[i].strip().lower()
        vocabulary.add(word)

    text_lines = lines[n + 1: n + 1 + m]
    text = " ".join(text_lines)

    for p in ['.', ',', ':', ';', '-', "'", '"', '!', '?']:
        text = text.replace(p, ' ')

    words = text.lower().split()

    for w in words:
        if not vocabulary.mark_used(w):
            print("Some words from the text are unknown.")
            return

    if vocabulary.all_used():
        print("Everything is going to be OK.")
    else:
        print("The usage of the vocabulary is not perfect.")


if __name__ == '__main__':
    solve()