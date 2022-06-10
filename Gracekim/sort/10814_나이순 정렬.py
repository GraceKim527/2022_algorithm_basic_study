# 이 문제 사실 학교에서 내줘서 풀었다요 ㅎㅎ 
n = int(input())
member_list = []

for _ in range(n):
    age, name = map(str, input().split()) #map 함수, split()함수 써서 각각 받기.
    member_list.append((age, name)) #2차원 리스트로 받는다.

member_list.sort(key = lambda x: int(x[0])) # (age, name)중 age로만 비교

for i in member_list:
    print(i[0], i[1])