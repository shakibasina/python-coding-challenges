# codeforce: https://codeforces.com/problemset/problem/71/A

n = int(input())

for i in range(n):
    x = input()
    if len(x) > 10:
        print(x[0], len(x[1:-1]), x[-1], sep="")
    else:
        print(x)