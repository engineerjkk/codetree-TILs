import sys
input = sys.stdin.readline
lst=list(map(str,input().strip()))

# cnt=0
# for i in range(len(lst)-1,-1,-1):
#     if lst[i]==")":
#         cnt+=1
# print(cnt)

print(((len(lst)-2)//2))