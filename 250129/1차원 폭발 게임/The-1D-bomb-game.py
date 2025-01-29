import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bomb = []

for i in range(n):
    b = int(input())
    bomb.append(b)

# print(bomb)
count = [0]*len(bomb)

def counts(st):
    cnt = 1
    if m==1:
        for i in range(len(bomb)):
            count[i] = 1
        return


    for i in range(st, len(bomb)-1):
        if bomb[i] == bomb[i+1] and bomb[i] !=0:
            cnt +=1
        else:
            break

    if cnt >= m :
        for i in range(st, st+cnt):
            count[i] = cnt
    return



def delete_zero():

    for i in range(len(count)):
        if count[i] != 0:
            count[i] = -1

def update_bomb():
    global bomb
    b = []
    for i in range(len(count)):
        if count[i] ==0:
            b.append(bomb[i])
    bomb = b



while True:
    count = [0]*len(bomb)
    prev_bomb = bomb[:]

    for i in range(len(bomb)):
        counts(i)

    delete_zero()
    update_bomb()

    if bomb==prev_bomb:
        break

print(len(bomb))
for x in bomb:
    print(x)