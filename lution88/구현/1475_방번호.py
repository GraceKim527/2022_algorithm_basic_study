a = input()

num = [0] * 10
num_6_9 = 0

for i in a:
    if i == '6' or i == '9':
        num_6_9 += 1
    else:
        num[int(i)] += 1

if num_6_9 % 2 == 0:
    num_6_9 = num_6_9 // 2
else:
    num_6_9 = num_6_9 // 2 + 1

num[6] = num_6_9

print(max(num))