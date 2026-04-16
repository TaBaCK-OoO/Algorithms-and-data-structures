import sys

BRACKETS = {"(": ")", "[": "]", "{": "}"}


def check_brackets(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        else:
            if len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    sequence = sys.stdin.read().strip()

    if sequence:
        res = check_brackets(sequence)
        print("yes" if res else "no")
    else:
        print("yes")