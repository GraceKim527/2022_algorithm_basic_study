# 이 문제 나 시간 초과만 두 번 떴다...
import sys # 얘가 최고. 

n = int(input())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline())) #input대신 sys.stdin.readline()으로 받는다.

lst.sort() #파이썬은 대단했다 sort라는게 있는게.
for i in lst:
    print(i)
