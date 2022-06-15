a = input()
index = len(a)//2

left = a[index:]
left_num = 0
right = a[:index]
right_num = 0

for i in range(index):
    left_num += int(left[i])
    right_num += int(right[i])
if left_num == right_num:
    print("LUCKY")
else:
    print("READY")