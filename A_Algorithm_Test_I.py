from math import factorial


N = int(input())
arr = set(map(int,input().split()))
print(factorial(len(arr)))