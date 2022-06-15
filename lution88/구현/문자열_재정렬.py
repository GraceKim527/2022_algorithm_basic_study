"""
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
"""

a = input()

def solution(a):
    # 입력받은 a의 원소가 알파벳이면 string에 담는다.
    string = [i for i in a if i.isalpha()]
    # 입력받은 a의 원소가 알파벳이 아닌경우 int로 감싸서 num에 담는다.
    num = map(int, [i for i in a if not i.isalpha()])
    # string 오름차순
    string.sort()
    # 입력받은 num 리스트의 모든 값을 더한다
    k = sum(num)
    # k의 값을 문자열로 변환하고 string 리스트에 append
    string.append(str(k))
    # string 리스트를 문자열 한 줄로 바꿔준다.
    answer = ''.join(string)
    return answer

print(solution(a))