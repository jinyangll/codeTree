import sys
input = sys.stdin.readline

a = input().strip()
l = len(a)

run = []
# print(run)

def encoding():
    global a
    temp = a[-1]

    for i in range(l-1):
        temp += a[i]
    a = temp
    return temp

def count_length(k):
    s = ""
    cnt = 1
    for i in range(len(k)-1):
        if k[i] == k[i+1]:
            cnt+=1
        else :
            s += k[i]
            s+= str(cnt)
            cnt = 1

    s += k[-1]
    s+= str(cnt)
    return s


for i in range(l):
    t = encoding()
    run.append(t)

# print(run)
ans = []
for x in run:
    s = count_length(x)
    ans.append(len(s))

print(min(ans))