## 1번째

# # 변수 정의
# N = input();    # 점수 N. 항상 짝수
# N_lenh = len(N)/2;  # N의 자릿수의 절반
# N_left = int(N) // 10**N_lenh # N의 왼쪽
# N_right = int(N) % 10**N_lenh # N의 오른쪽
# left = 0; # 왼쪽 부분 각 자릿수의 합 더한 값 저장
# right = 0; #오른쪽 부분 각 자릿수의 합 더한 값 저장

# # 
# for i in reversed(range(N_lenh)):
#     left += N_left // 10 ** i
#     N_left = N_left - 10 ** i

# for i in reversed(range(N_lenh)):
#     right += N_right // 10 ** i
#     N_right = N_right - 10 ** i


# if left == right:
#     print("LUCKY")
# else:
#     print("READY")




# ## 2번째

# # 변수 정의
# N = input();    # 점수 N. 항상 짝수
# N_lenh = int(len(N)/2);  # N의 자릿수의 절반
# N_left = int(N) // 10**N_lenh # N의 왼쪽
# N_right = int(N) % 10**N_lenh # N의 오른쪽
# left = 0; # 왼쪽 부분 각 자릿수의 합 더한 값 저장
# right = 0; #오른쪽 부분 각 자릿수의 합 더한 값 저장

# # 
# for i in reversed(range(N_lenh)):
#     left += N_left // 10 ** i
#     N_left = N_left - (10 ** i)

# for i in reversed(range(N_lenh)):
#     right += N_right // 10 ** i
#     N_right = N_right - 10 ** i


# if left == right:
#     print("LUCKY")
# else:
#     print("READY")



## 3번째

# 변수 정의
N = input();    # 점수 N. 항상 짝수
N_lenh = int(len(N)/2);  # N의 자릿수의 절반
N_left = int(N) // 10**N_lenh # N의 왼쪽
N_right = int(N) % 10**N_lenh # N의 오른쪽
left = 0; # 왼쪽 부분 각 자릿수의 합 더한 값 저장
right = 0; #오른쪽 부분 각 자릿수의 합 더한 값 저장

# 
for i in reversed(range(N_lenh)):
    left += N_left // 10 ** i
    N_left = N_left - (10 ** i)*(N_left // 10 ** i)

for i in reversed(range(N_lenh)):
    right += N_right // 10 ** i
    N_right = N_right - (10 ** i)*(N_right // 10 ** i)


if left == right:
    print("LUCKY")
else:
    print("READY")



