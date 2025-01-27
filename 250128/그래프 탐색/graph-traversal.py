import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


def dfs(v):
    global count
    count +=1
    visited[v] = True
    for nv in graph[v]:
        if visited[nv] == False:
            dfs(nv)


count = 0
dfs(1)

print(count-1)