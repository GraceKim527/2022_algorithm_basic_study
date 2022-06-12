# 선택 정렬로 풀어보기
n = int(input())

array = [] # 리스트 설정

for i in range(n):
    array.append(int(input())) # 받는 데이터 리스트에 모두 저장

for i in range(len(array)): 
    min_index = i                       # 리스트 첫번째 인덱스부터 min_index로 설정
    for j in range(i + 1, len(array)):  # 그 다음 인덱스부터 뽑아서 
        if array[min_index] > array[j]: # 만약 min_index 값이 더 크면 
            min_index = j               # j로 min_index 교체
    array[i], array[min_index] = array[min_index], array[i] # 그래서 min_index가 정해지면, 리스트 첫번째 인덱스 값과 교체

for i in array:
    print(i)
