# Link: https://www.acmicpc.net/problem/14501

def DFS(L, time, sum):
    global maxi
    if time > N+1:
        return

    if time <= N+1:
        maxi = max(maxi, sum)

        DFS(time + ti[L], sum + pi[L])
    DFS(time, sum)


if __name__ == "__main__":
    N = int(input())

    ti = [0]
    pi = [0]
    for i in range(N):
        tmp = list(map(int, input().split()))
        print(tmp)
        ti.append(tmp[0])
        pi.append(tmp[1])

    maxi = 0
    DFS(0, 0, 0)
    print(maxi)
