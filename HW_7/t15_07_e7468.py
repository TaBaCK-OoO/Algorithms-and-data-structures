import sys


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

    def ReorderList(self) -> None:

        if not self.head or not self.head.next:
            return

        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

            second_half = prev

        first_half = self.head
        while second_half:
            next_first = first_half.next
            next_second = second_half.next

            first_half.next = second_half
            second_half.next = next_first

            first_half = next_first
            second_half = next_second

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        self.tail = curr_node

    def Print(self) -> None:
        curr = self.head
        while curr:
            sys.stdout.write(str(curr.data) + " ")
            curr = curr.next
        sys.stdout.write("\n")


def solve():
    raw_data = sys.stdin.read().split()
    if len(raw_data) < 2:
        return

    n = int(raw_data[0])
    my_list = List()

    for i in range(1, n + 1):
        my_list.addToTail(int(raw_data[i]))

    my_list.ReorderList()
    my_list.Print()


if __name__ == '__main__':
    solve()