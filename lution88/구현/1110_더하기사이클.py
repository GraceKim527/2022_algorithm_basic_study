num = input()
first_num = num
cnt = 0

while True:
  if len(num) <= 1:
    left_num = 0
    right_num = num
  else:
    left_num = num[0]
    right_num = num[1]
  total = int(left_num) + int(right_num)
  right_total = str(total)[-1]
  new_num = str(right_num) + right_total
  num = new_num
  cnt += 1
  if int(new_num) == int(first_num):
    print(cnt)
    break
