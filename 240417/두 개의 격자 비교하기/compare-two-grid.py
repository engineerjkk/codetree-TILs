import sys 
input = sys.stdin.readline

n,m=map(int,input().split())

graph1=[]
for _ in range(n):
    graph1.append(list(map(int,input().split())))

graph2=[]
for _ in range(n):
    graph2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph1[i][j]==graph2[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()