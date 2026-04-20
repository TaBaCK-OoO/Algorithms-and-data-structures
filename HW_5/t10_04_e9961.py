def solve(available_nums: list[int], current_perm: list[int], k: int):
    if len(current_perm) == k:
        print(" ".join(map(str, current_perm)))
        return

    for i in range(len(available_nums)):
        sub_nums = available_nums[:i] + available_nums[i + 1:]

        solve(sub_nums, current_perm + [available_nums[i]], k)


if __name__ == "__main__":
    n, k = map(int, input().split())

    initial_nums = list(range(1, n + 1))

    solve(initial_nums, [], k)
