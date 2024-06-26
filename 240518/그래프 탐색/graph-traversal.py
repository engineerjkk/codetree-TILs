import sys
input = sys.stdin.readline
n,m = tuple(map(int,input().split()))
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]

vertex_cnt=0
def dfs(vertex):
    global vertex_cnt
    for node in graph[vertex]:
        if not visited[node]:
            visited[node]=True
            vertex_cnt+=1
            dfs(node)


for _ in range(m):
    a,b=tuple(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited[1]=True
dfs(1)
print(vertex_cnt)