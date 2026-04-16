import sys

sys.setrecursionlimit(2000)


def parse_class(cls_str):
    num = int(cls_str[:-1])
    letter = cls_str[-1]
    return num, letter


def is_less(stu1, stu2):
    if stu1[0] != stu2[0]:
        return stu1[0] < stu2[0]

    if stu1[1] != stu2[1]:
        return stu1[1] < stu2[1]

    return stu1[2] < stu2[2]


def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    mid = low + (high - low) // 2
    arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if is_less(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    students = []

    idx = 1
    for _ in range(n):
        last_name = input_data[idx]
        first_name = input_data[idx + 1]
        cls_str = input_data[idx + 2]
        dob = input_data[idx + 3]
        idx += 4

        c_num, c_letter = parse_class(cls_str)
        students.append((c_num, c_letter, last_name, first_name, dob, cls_str))

    if students:
        quick_sort(students, 0, len(students) - 1)

    for stu in students:
        print(f"{stu[5]} {stu[2]} {stu[3]} {stu[4]}")


if __name__ == '__main__':
    solve()