"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

EMPTY = "EMPTY"
DELETED = "DELETED"


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class CatalogHashTable:
    M = 31

    def __init__(self, size=11):
        self.size: int = size
        self.keys: list = [EMPTY for _ in range(size)]
        self.values: list = [EMPTY for _ in range(size)]
        self.count: int = 0

    def hash(self, key: str):
        h = 0
        for char in key:

            h = (h * self.M + ord(char)) % self.size
        return h

    def rehash(self):
        old_keys = self.keys
        old_values = self.values

        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        self.keys = [EMPTY for _ in range(self.size)]
        self.values = [EMPTY for _ in range(self.size)]
        self.count = 0

        for i in range(len(old_keys)):
            k = old_keys[i]
            if k is not EMPTY and k is not DELETED:
                self._insert_existing(k, old_values[i])

    def _insert_existing(self, key: str, val_list: list):
        i = self.hash(key)
        while self.keys[i] is not EMPTY and self.keys[i] is not DELETED:
            i = (i + 1) % self.size
        self.keys[i] = key
        self.values[i] = val_list
        self.count += 1

    def add_book(self, author: str, title: str):
        if self.count > 0.7 * self.size:
            self.rehash()

        i = self.hash(author)
        first_deleted = -1

        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                for existing_title in self.values[i]:
                    if existing_title == title:
                        return
                self.values[i].append(title)
                return
            elif self.keys[i] is DELETED and first_deleted == -1:
                first_deleted = i

            i = (i + 1) % self.size


        insert_idx = first_deleted if first_deleted != -1 else i
        self.keys[insert_idx] = author
        self.values[insert_idx] = [title]
        self.count += 1

    def find_book(self, author: str, title: str):
        i = self.hash(author)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                for existing_title in self.values[i]:
                    if existing_title == title:
                        return True
                return False
            i = (i + 1) % self.size
        return False

    def delete_book(self, author: str, title: str):
        i = self.hash(author)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                for idx in range(len(self.values[i])):
                    if self.values[i][idx] == title:
                        self.values[i].pop(idx)
                        if len(self.values[i]) == 0:
                            self.keys[i] = DELETED
                            self.values[i] = DELETED
                            self.count -= 1
                        return
                return
            i = (i + 1) % self.size

    def find_by_author(self, author: str):
        i = self.hash(author)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == author:
                # Сортуємо книги за умовою
                return sorted(self.values[i])
            i = (i + 1) % self.size
        return []


catalog = None


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global catalog
    catalog = CatalogHashTable()


def addBook(author, title):
    """ Додає книгу до бібліотеки. """
    catalog.add_book(author, title)


def find(author, title):
    """ Перевіряє чи міститься задана книга у бібліотеці. """
    return catalog.find_book(author, title)


def delete(author, title):
    """ Видаляє книгу з бібліотеки. """
    catalog.delete_book(author, title)


def findByAuthor(author):
    """ Повертає список книг заданого автора. """
    return catalog.find_by_author(author)