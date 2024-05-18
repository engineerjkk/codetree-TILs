import sys
input = sys.stdin.readline
n,m = map(int,input().split())

visited=[False for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

vertex_cnt=0
def dfs(vertex):
    global vertex_cnt
    if not visited[vertex]:
        for node in graph[vertex]:
                visited[node]=True
                vertex_cnt+=1
                dfs(node)

for _ in range(m):
    a,b=tuple(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(vertex_cnt)