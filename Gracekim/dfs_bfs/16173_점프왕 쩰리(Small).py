from collections import deque

# BFS
def bfs(x, y, visited):
    queue = deque() # queue를 구현하기 위해 deque 라이브러리 사용
    #deque는 양방향 큐, 즉 앞 뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거가 가능하다.
    queue.append((x, y))
    visited[x][y] = True
    
    #queue가 빌 때까지
    while queue:
        x, y = queue.popleft() # 좌표
        if array[x][y] == -1: # -1이 도착지점
            return 'HaruHaru'
        for i in range(n-1):
            nx = x + dx[i] * array[x][y] #현재 밟고 있는 수만큼 이동
            ny = y + dy[i] * array[x][y] #현재 밟고 있는 수만큼 이동
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == True:
                continue

            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return 'Hing'
    
n = int(input())
array = []
for _ in range(n): #2차원 리스트
    array.append(list(map(int, input().split())))

visited = []
for _ in range(n): 
    visited.append([False]*n) # n * n False삽입

dx = [1, 0]
dy = [0, 1]

print(bfs(0, 0, visited))