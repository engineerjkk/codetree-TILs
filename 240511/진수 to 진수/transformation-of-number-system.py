import sys
input = sys.stdin.readline
a,b = map(int,input().split())
value = str(input())

if a ==2:
    tmp = int('0b'+value,2)
elif a == 8:
    tmp = int('0o'+value,8)

if b == 2:
    print(bin(tmp)[2:])
elif b == 8:
    print(oct(tmp)[2:])