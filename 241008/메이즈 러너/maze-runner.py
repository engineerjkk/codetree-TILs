import sys
input = sys.stdin.readline
N,M,K=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))
next_space=[[0]*N for _ in range(N)]
traveler=[]
for _ in range(M):
    r,c=map(int,input().split())
    traveler.append((r-1,c-1))
er,ec=map(int,input().split())
Exit=(er-1,ec-1)
sr,sc,square_size=0,0,0
ans=0

def move_traveler():
    global ans,Exit
    for i in range(M):
        if traveler[i]==Exit:
            continue
        tr,tc=traveler[i]
        er,ec=Exit
        if tr!=er:
            nr,nc=tr,tc
            if er>tr:
                nr+=1
            else:
                nr-=1
            if space[nr][nc]==0:
                traveler[i]=(nr,nc)
                ans+=1
                continue
        if tc!=ec:
            nr,nc=tr,tc
            if ec>tc:
                nc+=1
            else:
                nc-=1
            if space[nr][nc]==0:
                traveler[i]=(nr,nc)
                ans+=1
                continue

def find_minimum_square():
    global sr,sc,square_size,Exit
    er,ec=Exit
    for size in range(2,N+1):
        for start_r in range(N-size+1):
            for start_c in range(N-size+1):
                end_r,end_c=start_r+size-1,start_c+size-1
                if not (start_r<=er<=end_r and start_c<=ec<=end_c):
                    continue
                is_in_traveler=False
                for i in range(M):
                    tr,tc=traveler[i]
                    if start_r<=tr<=end_r and start_c<=tc<=end_c:
                        if not (tr==er and tc==ec):
                            is_in_traveler=True
                if is_in_traveler:
                    sr=start_r
                    sc=start_c
                    square_size=size
                    return 

def rotate_square():
    for i in range(sr,sr+square_size):
        for j in range(sc,sc+square_size):
            if space[i][j]>0:
                space[i][j]-=1
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            Or,Oc=r-sr,c-sc
            rr,rc=Oc,square_size-Or-1
            next_space[sr+rr][sc+rc]=space[r][c]
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            space[r][c]=next_space[r][c]

def rotate_traveler_and_Exit():
    global Exit
    for i in range(M):
        tr,tc=traveler[i]
        if sr<=tr<sr+square_size and sc<=tc<sc+square_size:
            Or,Oc=tr-sr,tc-sc
            rr,rc=Oc,square_size-Or-1
            traveler[i]=(sr+rr,sc+rc)
    er,ec=Exit
    if sr<=er<sr+square_size and sc<=ec<sc+square_size:
        Or,Oc=er-sr,ec-sc
        rr,rc=Oc,square_size-Or-1
        Exit=(sr+rr,sc+rc)
    return
                




for _ in range(K):
    move_traveler()
    all_traveler_is_escaped=True
    for i in range(M):
        if traveler[i]!=Exit:
            all_traveler_is_escaped=False
    if all_traveler_is_escaped:
        break
    find_minimum_square()
    rotate_square()
    rotate_traveler_and_Exit()
print(ans)
print(Exit[0]+1,Exit[1]+1)