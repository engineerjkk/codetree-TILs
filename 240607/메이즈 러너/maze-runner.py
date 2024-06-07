import sys
input = sys.stdin.readline
n,m,k=map(int,input().split())
space=[[0]*(n+1) for _ in range(n+1)]
next_space=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    space[i][1:]=map(int,input().split())
traveler=[[-1,-1]]
for _ in range(m):
    traveler.append(list(map(int,input().split())))
exits=list(map(int,input().split()))
ans=0

def move_all_traveler():
    global exits, ans
    for i in range(1,m+1):
        if traveler[i]==exits:
            continue
        tr,tc=traveler[i]
        er,ec=exits
        if er!=tr:
            nr,nc=tr,tc
            if er>tr:
                nr+=1
            else:
                nr-=1
            if space[nr][nc]==0:
                traveler[i]=[nr,nc]
                ans+=1
                continue
        if ec!=tc:
            nr,nc=tr,tc
            if ec>tc:
                nc+=1
            else:
                nc-=1
            if space[nr][nc]==0:
                traveler[i]=[nr,nc]
                ans+=1
                continue

def find_minimum_square():
    global exits,sr,sc,square_size
    er,ec=exits
    for size in range(2,n+1):
        for start_r in range(1,n-size+2):
            for start_c in range(1,n-size+2):
                end_r,end_c=start_r+size-1,start_c+size-1
                if not (start_r<=er<=end_r and start_c<=ec<=end_c):
                    continue
                is_traveler_in=False
                for i in range(1,m+1):
                    tr,tc=traveler[i]
                    if start_r<=tr<=end_r and start_c<=tc<=end_c:
                        if not(er==tr and ec==tc):
                            is_traveler_in=True
                if is_traveler_in:
                    sr=start_r
                    sc=start_c
                    square_size=size
                    return

def rotate_square():
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            if space[r][c]:
                space[r][c]-=1
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size): 
            Or,Oc=r-sr,c-sc
            rr,rc=Oc,square_size-Or-1
            next_space[sr+rr][sc+rc]=space[r][c]
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size): 
            space[r][c]=next_space[r][c]

def rotate_traveler_and_exits():
    global exits
    for i in range(1,m+1):
        tr,tc=traveler[i]
        if sr<=tr<sr+square_size and sc<=tc<sc+square_size:
            Or,Oc=tr-sr,tc-sc
            rr,rc=Oc,square_size-Or-1
            traveler[i]=[sr+rr,sc+rc]
    er,ec=exits
    if sr<=er<sr+square_size and sc<=ec<sc+square_size:
        Or,Oc=er-sr,ec-sc
        rr,rc=Oc,square_size-Or-1
        exits=[sr+rr,sc+rc]

                

for _ in range(k):
    move_all_traveler()
    is_all_escaped=True
    for i in range(1,m+1):
        if traveler[i]!=exits:
            is_all_escaped=False
    if is_all_escaped:
        break
    find_minimum_square()
    rotate_square()
    rotate_traveler_and_exits()
print(ans)
print(*exits)