# codeforce: https://codeforces.com/problemset/problem/282/A

n = int(input())
x = 0
for _ in range(n):
    c = input()
    if "++" in c:
        x += 1
    elif "--" in c:
        x -= 1

print(x)
