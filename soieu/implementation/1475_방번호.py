# 변수 선언
N = input()
N_len = len(N)
n_set_basic = [1,2,3,4,5,6,7,8,9,0] # 숫자 한 세트
n_set = [1,2,3,4,5,6,7,8,9,0] # 숫자 한 세트
num = 0 # 지금 보는 숫자
count = 1 # 출력할 값. 필요한 세트의 개수의 최솟값
N = int(N)

#
for i in reversed(range(N_len)):
    num = N // 10 ** i # 맨 앞부터 숫자 확인 
    N = N - (10 ** i)*(N // 10 ** i)

    if n_set.count(num) != 0:
        n_set.remove(num)
    else:
        if num == 6:
            if n_set.count(9) != 0:
                n_set.remove(9)
            else:
                count += 1
                n_set = n_set + n_set_basic
                n_set.remove(6)
        elif num == 9:
            if n_set.count(6) != 0:
                n_set.remove(6)
            else:
                count += 1
                n_set = n_set + n_set_basic
                n_set.remove(9)
        else:
            count += 1
            n_set = n_set + n_set_basic
            n_set.remove(num)

print(count)