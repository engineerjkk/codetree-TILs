import sys
input = sys.stdin.readline
from collections import deque
dr=[-1,0,1,0]
dc=[0,1,0,-1]
N,M,K=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))

teams=[]
def in_range(r,c):
    return -1<r<N and -1<c<N
for i in range(N):
    for j in range(N):
        if space[i][j]==1:
            queue=deque()
            queue.append((i,j))
            trace=deque()
            trace.append((i,j))
            visit=[[False]*N for _ in range(N)]
            visit[i][j]=True
            while queue:
                r,c=queue.popleft()
                for k in range(4):
                    nr=r+dr[k]
                    nc=c+dc[k]
                    if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==2:
                        visit[nr][nc]=True
                        queue.append((nr,nc))
                        trace.append((nr,nc))
            r,c=trace[-1]
            for k in range(4):
                nr=r+dr[k]
                nc=c+dc[k]
                if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==3:
                    trace.append((nr,nc))
                    break
            teams.append(trace)

def move():
    for team in teams:
        print(team)
        r,c=team.popleft()
        space[r][c]=4
        space[team[-1][0]][team[-1][1]]=3
        
        r,c=team[0]
        space[r][c]=2
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and space[nr][nc]==4:
                space[nr][nc]=1
                team.appendleft((nr,nc))
                break
def ball(idx):
    idx=idx%(4*N)
    if idx<N:
        for c in range(N):
            if space[idx][c] in (1,2,3):
                return (idx,c)
    elif idx<2*N:

        for r in reversed(range(N)):
            if space[r][idx-N] in (1,2,3):
                return (r,idx-N)
    elif idx<3*N:
        for c in reversed(range(N)):
            if space[3*N-1-idx][c] in (1,2,3):
                return (3*N-1-idx,c)
    else:

        for r in range(N):
            if space[r][4*N-1-idx] in (1,2,3):
                return (r,4*N-1-idx)
    return (-1,-1)

def change(r,c):
    if r==-1 and c==-1:
        return 0
    for i in range(M):
        if (r,c) in teams[i]:
            for j in range(len(teams[i])):
                if teams[i][j]==(r,c):
                    space[teams[i][0][0]][teams[i][0][1]]=3
                    space[teams[i][-1][0]][teams[i][-1][1]]=1
                    teams[i].reverse()
                    return (j+1)**2

cnt=0
for i in range(K):
    move()
    a,b=ball(i)
    cnt+=change(a,b)
print(cnt)
                    
'''idx = idx % (4 * N) 대신 idx = idx % 4로 변경하면 문제가 발생할 수 있습니다. 이를 이해하기 위해서 함수의 작동 방식과 공 던지기의 방향을 다시 한번 살펴보겠습니다.

공 던지기 방식
공 던지기 함수 ball은 라운드 번호 idx에 따라 다음 네 가지 방향으로 공을 던집니다:

첫 번째 방향: 위에서 아래로 (첫 번째 행을 왼쪽에서 오른쪽으로)
두 번째 방향: 오른쪽에서 왼쪽으로 (첫 번째 열을 아래에서 위로)
세 번째 방향: 아래에서 위로 (마지막 행을 오른쪽에서 왼쪽으로)
네 번째 방향: 왼쪽에서 오른쪽으로 (마지막 열을 위에서 아래로)
이 네 가지 방향을 반복하기 위해 idx를 0부터 4 * N - 1까지의 값으로 제한합니다. 이는 라운드 번호 idx가 전체 보드의 크기 N을 기준으로 각 방향을 모두 한 번씩 포함하도록 하기 위함입니다.

왜 4 * N인가?
각 방향은 N번 반복됩니다. 따라서 총 4 * N 라운드가 필요합니다:

첫 번째 방향 (위에서 아래로): 0에서 N-1
두 번째 방향 (오른쪽에서 왼쪽으로): N에서 2N-1
세 번째 방향 (아래에서 위로): 2N에서 3N-1
네 번째 방향 (왼쪽에서 오른쪽으로): 3N에서 4N-1
이처럼 각 방향은 N번 반복되고, 총 4개의 방향이 있으므로 4 * N입니다.

왜 idx % 4는 안 되는가?
idx % 4는 0에서 3까지의 값만을 반환합니다. 이는 네 가지 방향만을 고려하지만, 각 방향 내에서의 위치를 고려하지 않습니다. 예를 들어, idx = 5인 경우 idx % 4 = 1이 되어 두 번째 방향을 나타내지만, 실제로는 다섯 번째 위치에서의 던지기가 되어야 합니다. 이를 반영하기 위해서는 idx % (4 * N)을 사용하여 전체 라운드를 네 가지 방향으로 나누고, 각 방향 내에서의 위치를 정확히 계산해야 합니다.

예제
다음은 idx % 4와 idx % (4 * N)의 차이를 예시로 설명합니다:

N = 3인 경우:
idx = 5일 때:
idx % 4 = 1: 두 번째 방향 (오른쪽에서 왼쪽으로), 위치는 잘못 계산됨.
idx % (4 * N) = 5: 올바른 방향 및 위치 계산.
따라서 idx % 4 대신 idx % (4 * N)을 사용하여 네 가지 방향과 각 방향 내에서의 위치를 정확히 고려해야 합니다.

정리
idx = idx % (4 * N)은 라운드 번호 idx를 0부터 4 * N - 1까지로 제한하여 각 방향을 정확히 다루고, 각 방향 내에서의 위치를 올바르게 계산합니다. 이는 공 던지기 방향과 각 방향 내에서의 위치를 일치시키기 위한 필수적인 계산입니다.
'''