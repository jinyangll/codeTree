import sys
input = sys.stdin.readline

k, n = map(int, input().split())

path = []

def back_tracking(x):

    if x == n:
        print(*path)
        return

    for i in range(1,k+1):
        path.append(i)
        back_tracking(x+1)
        path.pop()

back_tracking(0)