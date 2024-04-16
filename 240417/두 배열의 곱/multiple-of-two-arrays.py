import sys 
input = sys.stdin.readline
graph1=[]
for _ in range(3):
    graph1.append(list(map(int,input().split())))
input()
graph2=[]
for _ in range(3):
    graph2.append(list(map(int,input().split())))

#ans=[[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        print(graph1[i][j]*graph2[i][j], end=" ")
    print()