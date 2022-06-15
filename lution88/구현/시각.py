# 정수 입력
n = int(input())
# 3이 들어간 숫자 카운트
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                print(f'{str(i)}:{str(j)}:{str(k)}', cnt)

print(cnt)