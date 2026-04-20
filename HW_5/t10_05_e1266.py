import sys

best_sum: int = 0
best_subset: list[int] = []
found_exact: bool = False


def solve(available_tracks: list[int], current_subset: list[int], current_sum: int, max_n: int, rem_sum: int):
    global best_sum, best_subset, found_exact

    if found_exact or current_sum > max_n:
        return

    if current_sum > best_sum:
        best_sum = current_sum
        best_subset = current_subset
        if best_sum == max_n:
            found_exact = True
            return
    if current_sum + rem_sum <= best_sum:
        return

    current_rem = rem_sum
    for i in range(len(available_tracks)):
        current_rem -= available_tracks[i]

        sub_tracks = available_tracks[i + 1:]

        solve(sub_tracks, current_subset + [available_tracks[i]], current_sum + available_tracks[i], max_n, current_rem)


if __name__ == "__main__":
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if not parts:
            continue

        max_n = parts[0]
        tracks = parts[2:]

        best_sum = 0
        best_subset = []
        found_exact = False

        solve(tracks, [], 0, max_n, sum(tracks))

        if best_subset:
            print(f"sum:{best_sum}")