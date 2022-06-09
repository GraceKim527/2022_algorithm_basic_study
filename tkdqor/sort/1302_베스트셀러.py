from collections import Counter # 리스트안에 데이터 중복 횟수 구하기 위해 Counter import
n = int(input())

array = [] # 리스트 지정

for i in range(n):        # 받은 데이터 리스트에 모두 추가
    array.append(input())

array = sorted(array) # 리스트 정렬로 오름차순 만들어놓기

counter = Counter(array)   # Counter 사용해서 중복 제거하고
array_dict = dict(counter) # 딕셔너리로 만들기

book = []  # 딕셔너리의 key와 value를 따로 저장하기 위해 리스트 2개 지정
count = []

for key, value in array_dict.items(): # 딕셔너리에서 key와 value를 각각 book과 count라는 리스트에 저장
    book.append(key)                  # book에는 책의 제목이 들어가고
    count.append(value)               # count에는 책의 개수가 들어가게 하기

max_count = max(count)                # 책의 개수 중에서 가장 큰 수를 max_count라고 지정
book_index = (count.index(max_count)) # count 리스트에서 가장 큰 수의 인덱스를 구해서 book_index라고 지정
print(book[book_index])               # book 리스트에서 해당 인덱스로 가장 많이 팔린 책 제목 출력









