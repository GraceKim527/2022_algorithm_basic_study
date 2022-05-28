from collections import deque
import sys

read = sys.stdin.readline # input과 같은 기능, 시간이 더 빠르다.
n, m, v = map(int, read().split())

# 방문 체크
visited = [0] * (n + 1)

# 인접 영행렬 영으로만 이루어진 행렬이며, 바뀔경우엔 1을 추가하는 식이다.
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 입력 받는 값을 영행렬에 1 삽입
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    # 방문 표시
    visited[v] = 1
    print(v, end=' ')

    # 재귀 함수 (인접한 곳을 방문하지 않은 경우에 함수가 실행)
    for i in range(1, n+1):
        if(visited[i] == 0 and graph[v][i] == 1):
            dfs(i)

def bfs(v):
    # 방문 큐
    queue = [v]
    # dfs를 완료하고 나서의 visited 배열을 다시 0으로 방문체크한다.
    visited[v] = 0

    # 데이터가 없어질 때 까지
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if(visited[i] == 1 and graph[v][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)