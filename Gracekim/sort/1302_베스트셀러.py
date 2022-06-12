import sys

n = int(sys.stdin.readline())
store = dict()

for i in range(n):
    book = sys.stdin.readline().rstrip()
    if book in store:
        store[book] += 1
    else:
        store[book] = 1

store = sorted(store.items(), key = lambda x: (-x[1], x[0]))

print(store[0][0])