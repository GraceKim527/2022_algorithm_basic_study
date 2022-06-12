import sys

num = int(sys.stdin.readline())
new_num = [int(sys.stdin.readline()) for _ in range(num)]

for i in range(1, len(new_num)):
    for j in range(i, 0, -1):
        if new_num[j] < new_num[j-1]:
            new_num[j], new_num[j-1] = new_num[j-1], new_num[j]
        else:
            break

for i in new_num:
    print(i)