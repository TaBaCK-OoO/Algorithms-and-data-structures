import sys

sys.set_int_max_str_digits(200000)


def karatsuba_str(x_str: str, y_str: str) -> int:
    if len(x_str) == 1 and len(y_str) == 1:
        return int(x_str) * int(y_str)

    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    m = max_len // 2

    high1, low1 = x_str[:-m], x_str[-m:]
    high2, low2 = y_str[:-m], y_str[-m:]

    if not high1: high1 = "0"
    if not high2: high2 = "0"

    z0 = karatsuba_str(low1, low2)
    z2 = karatsuba_str(high1, high2)

    sum_x = str(int(low1) + int(high1))
    sum_y = str(int(low2) + int(high2))
    z1 = karatsuba_str(sum_x, sum_y) - z2 - z0

    return (z2 * 10 ** (2 * m)) + (z1 * 10 ** m) + z0


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        A_str = input_data[0]
        B_str = input_data[1]

        result = karatsuba_str(A_str, B_str)
        print(result)