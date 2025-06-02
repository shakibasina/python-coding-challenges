# codeforces: https://codeforces.com/problemset/problem/231/A

n = int(input())
r = 0
for _ in range(n):
    x = input()
    if x.count("1") >= 2:
        r += 1
    i += 1
print(r)
