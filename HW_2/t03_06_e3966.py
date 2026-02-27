'''
7
10 47 50 63 89 90 99
4
84 33 10 82

'''

def solve(array, x):
    l = 0
    r = len(array) - 1
    while l <= r:
        m = l + (r - l) // 2
        if array[m] == x:
            return "YES"
        elif array[m] < x:
            l = m + 1
        else:
            r = m - 1
    return "NO"

n = int(input())
collection = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))
results = []

for q in queries:
    results.append(solve(collection, q))

print("\n".join(results))