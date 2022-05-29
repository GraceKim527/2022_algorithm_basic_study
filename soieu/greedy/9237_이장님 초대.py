today = 2

# 나무모묙 n개
n = int(input())

# t 입력받기
list_t =[]
list_endday=[]

list_t = list(map(int,input().split()))

list_t.sort(reverse=True)

for days in list_t:
    list_endday.append(days+today)
    today+=1

print(max(list_endday))


