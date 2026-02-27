def find_first(array, x):
    l = 0
    r = len(array)
    while l < r:
        m = l + (r - l) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m
    return l

def solve(array, x):
    start = find_first(array, x)
    end = find_first(array, x + 1)
    return end - start

n = int(input())

if n == 0:
    input()
    array = []
else:
    array = list(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))

results = []

for i in range(m):
    ans = solve(array, queries[i])
    results.append(str(ans))

print("\n".join(results))