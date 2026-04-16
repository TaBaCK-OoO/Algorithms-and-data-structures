import sys

def prefix_to_infix(expression: str) -> str:
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for char in reversed(expression):
        if char.isalpha():
            stack.append((char, 3))
        elif char in precedence:
            left_expr, left_prec = stack.pop()
            right_expr, right_prec = stack.pop()

            op_prec = precedence[char]
            if left_prec < op_prec:
                left_expr = f"({left_expr})"
            if right_prec < op_prec or (right_prec == op_prec and char in ('-', '/')):
                right_expr = f"({right_expr})"

            stack.append((f"{left_expr}{char}{right_expr}", op_prec))

    return stack[0][0]

if __name__ == "__main__":
    input_expr = sys.stdin.read().strip()
    if input_expr:
        print(prefix_to_infix(input_expr))