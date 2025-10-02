# codeforces: https://codeforces.com/problemset/problem/112/A
# update

a = input().lower()
b = input().lower()

i = 0
while i < len(a):
    if ascii(a[i]) > ascii(b[i]):
        print(1)
        break
    elif ascii(a[i]) < ascii(b[i]):
        print(-1)
        break
    i += 1
else:
    print(0)
