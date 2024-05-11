import sys
input = sys.stdin.readline
a,b = map(int,input().split())
value = str(input())

tmp=int(value,a)

def solution(n,q):
    rev_base=''
    while n>0:
        n,mod=divmod(n,q)
        rev_base+=str(mod)
    return rev_base[::-1]
print(solution(tmp,b))