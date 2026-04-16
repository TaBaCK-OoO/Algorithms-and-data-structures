#Insertion Sort

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shifted = False

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifted = True

        arr[j + 1] = key

        if shifted:
            print(" ".join(map(str, arr)))


if __name__ == '__main__':
    solve()