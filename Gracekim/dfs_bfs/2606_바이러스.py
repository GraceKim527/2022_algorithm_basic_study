from collections import deque

n = int(input())
com_n = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(com_n):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1) # 네트워크는 양방향

def bfs(graph, v):
    global count
    queue = deque([v]) 

    while queue:
        pop = queue.popleft() # 기입된 요소를 pop
        visited[pop] = True # 방문했다고 체크
        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                count += 1
    print(count)

bfs(graph, 1)