import sys


class CardNode:
    __slots__ = ['value', 'next_node']

    def __init__(self, value):
        self.value = value
        self.next_node = None


class GameQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self, value):
        new_card = CardNode(value)
        if self.is_empty():
            self.head = new_card
        else:
            self.tail.next_node = new_card
        self.tail = new_card
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Cannot pop from an empty queue")

        removed_node = self.head
        card_val = removed_node.value
        self.head = self.head.next_node

        self.count -= 1
        if self.head is None:
            self.tail = None

        return card_val


def main():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return

    n = int(raw_data[0])
    half = n // 2

    player1 = GameQueue()
    player2 = GameQueue()

    for i in range(1, half + 1):
        player1.push(int(raw_data[i]))

    for i in range(half + 1, n + 1):
        player2.push(int(raw_data[i]))

    rounds = 0
    LIMIT = 200000

    while not player1.is_empty() and not player2.is_empty() and rounds < LIMIT:
        card1 = player1.pop()
        card2 = player2.pop()
        rounds += 1

        p1_wins_special = (card1 == 0 and card2 == n - 1)
        p2_wins_special = (card2 == 0 and card1 == n - 1)

        if p1_wins_special or (not p2_wins_special and card1 > card2):
            player1.push(card1)
            player1.push(card2)
        else:
            player2.push(card1)
            player2.push(card2)

    if rounds == LIMIT and not player1.is_empty() and not player2.is_empty():
        print("draw")
    elif player2.is_empty():
        print(f"first {rounds}")
    else:
        print(f"second {rounds}")


if __name__ == '__main__':
    main()