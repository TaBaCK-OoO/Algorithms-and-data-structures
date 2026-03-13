

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n: int):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class LibraryCatalog:
    def __init__(self, size=11):
        self.size = size
        self.keys = [EMPTY] * size
        self.values = [EMPTY] * size
        self.count = 0
        self.deleted_count = 0

    def hash_str(self, key: str):
        h = 0
        for char in key:
            h = (h * 31 + ord(char)) % self.size
        return h

    def rehash(self):
        old_size = self.size
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        old_keys = self.keys
        old_values = self.values

        self.keys = [EMPTY] * self.size
        self.values = [EMPTY] * self.size
        self.count = 0
        self.deleted_count = 0

        for i in range(old_size):
            k = old_keys[i]
            if k is not EMPTY and k is not DELETED:
                idx = self.hash_str(k)
                while self.keys[idx] is not EMPTY:
                    idx = (idx + 1) % self.size

                self.keys[idx] = k
                self.values[idx] = old_values[i]
                self.count += 1

    def add(self, author: str, title: str):
        if (self.count + self.deleted_count) > 0.7 * self.size:
            self.rehash()

        i = self.hash_str(author)
        first_deleted = -1

        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                if title not in self.values[i]:
                    self.values[i].append(title)
                return
            if self.keys[i] is DELETED and first_deleted == -1:
                first_deleted = i
            i = (i + 1) % self.size

        if first_deleted != -1:
            i = first_deleted
            self.deleted_count -= 1

        self.keys[i] = author
        self.values[i] = [title]
        self.count += 1

    def find(self, author: str, title: str):
        i = self.hash_str(author)
        start_i = i

        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                return title in self.values[i]
            i = (i + 1) % self.size
            if i == start_i:
                break
        return False

    def delete(self, author: str, title: str):
        i = self.hash_str(author)
        start_i = i

        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                if title in self.values[i]:
                    self.values[i].remove(title)
                return
            i = (i + 1) % self.size
            if i == start_i:
                break

    def find_by_author(self, author: str):
        i = self.hash_str(author)
        start_i = i

        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:

                res = self.values[i][:]
                res.sort()
                return res
            i = (i + 1) % self.size
            if i == start_i:
                break
        return []


catalog = None


def init():
    global catalog
    catalog = LibraryCatalog()


def addBook(author, title):
    catalog.add(author, title)


def find(author, title):
    return catalog.find(author, title)


def delete(author, title):
    catalog.delete(author, title)


def findByAuthor(author):
    return catalog.find_by_author(author)