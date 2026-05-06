import sys

# Збільшуємо ліміт рекурсії, щоб програма не впала при довгому списку
sys.setrecursionlimit(2000)


class Node:
    __slots__ = ['data', 'next']

    def __init__(self, data: int):
        self.data = data
        self.next = None


class List:
    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def Print(self) -> None:
        curr = self.head
        while curr:
            sys.stdout.write(str(curr.data) + " ")
            curr = curr.next
        sys.stdout.write("\n")

    def PrintReverse(self) -> None:
        # Використовуємо рекурсію замість заборонених масивів (list)
        def _reverse_recursive(node: Node) -> None:
            if node is None:
                return
            _reverse_recursive(node.next)
            sys.stdout.write(str(node.data) + " ")

        _reverse_recursive(self.head)
        sys.stdout.write("\n")


def solve():
    raw_data = sys.stdin.read().split()
    if len(raw_data) < 2:
        return

    n = int(raw_data[0])
    my_list = List()

    for i in range(1, n + 1):
        my_list.addToTail(int(raw_data[i]))

    my_list.Print()
    my_list.PrintReverse()


if __name__ == '__main__':
    solve()