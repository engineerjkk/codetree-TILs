import sys
input = sys.stdin.readline
n= int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
lst=sorted(lst,key=lambda x : (x[1],x[0]))

def greedy(lst):
    start_time=0
    count=0
    for i in range(len(lst)):
        start,end=lst[i]
        if start >=start_time:
            count+=1
            start_time=end
    return count
print(n-greedy(lst))