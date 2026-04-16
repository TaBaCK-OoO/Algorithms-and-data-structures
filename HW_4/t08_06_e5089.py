#Selection Sort

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    words = input_data[1:n + 1]

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if words[j] < words[min_index]:
                min_index = j

        words[i], words[min_index] = words[min_index], words[i]

    for word in words:
        print(word)


if __name__ == '__main__':
    solve()