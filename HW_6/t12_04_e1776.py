import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1

        if n == 0:
            break

        while idx < len(input_data):
            if input_data[idx] == '0':
                idx += 1
                print()
                break

            target = []
            for _ in range(n):
                target.append(int(input_data[idx]))
                idx += 1

            stack = []
            current_coach = 1
            possible = True

            for needed_coach in target:
                while current_coach <= needed_coach:
                    stack.append(current_coach)
                    current_coach += 1

                if len(stack) > 0 and stack[-1] == needed_coach:
                    stack.pop()
                else:
                    possible = False
                    break

            if possible:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    solve()