ekq =1


# bfs일까 dfs일까
def bfsdfs(i,j,map,n,visited):

    global ekq

    visited[i][j] = 1

    if map[i][j] == -1:
        ekq = 0
    else:
        if (i + map[i][j] < n) and (visited[i + map[i][j]][j] != 1):
            bfsdfs(i + map[i][j], j, map, n, visited)
        if (j + map[i][j] < n) and (visited[i][j + map[i][j]] != 1):
            bfsdfs(i , j+ map[i][j], map, n, visited)


# 게임구역 크기 입력(n*n)
n = int(input())

# 맵 입력&방문한곳선언 - 구글링으로 이차원 배열 선언과 동시에 입력받는거 알아냄
# https://dailylifeofdeveloper.tistory.com/132 참조
# 0은 방문안한곳 1은 방문한곳
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

bfsdfs(0,0,map,n,visited)

if ekq == 0:
    print("HaruHaru")
else:
    print("Hing")