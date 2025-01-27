import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def check_range(x,y) :
    return x>=0 and x<n and y>=0 and y<n

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*n for _ in range(n)]
q = deque()

for i in range(k):
    r, c = map(int, input().split())

    r-=1
    c-=1

    q.append([r,c])
    visited[r][c] = True

max_q = 0


while q:
    x, y= q.popleft()
    # max_q = max(max_q, cnt)

    for nx, ny in zip(dx,dy):
        cur_x = x+nx
        cur_y = y+ny
        if check_range(cur_x, cur_y) and grid[cur_x][cur_y] == 0 \
                and visited[cur_x][cur_y] == False:
            q.append([cur_x, cur_y])
            visited[cur_x][cur_y] = True
            # print(cur_x, cur_y, cnt+1)

cnt= 0
for x in visited:
    for i in x:
        if i == True:
            cnt+=1

print(cnt)
