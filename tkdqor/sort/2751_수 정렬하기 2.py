import sys
n = int(sys.stdin.readline()) # 큰 수를 받기 위해 sys 사용

array = [] # 리스트 선언

for i in range(n):                          # 입력받은 데이터를 리스트에 모두 추가
    array.append(int(sys.stdin.readline()))

array = sorted(array) # sorted 함수를 사용해서 정렬된 새로운 리스트를 저장 

for i in range(len(array)): # 리스트 데이터 1개씩 출력
    print(array[i])







