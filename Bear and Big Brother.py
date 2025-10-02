# codeforces: https://codeforces.com/problemset/problem/791/A
# update
a, b = input().split()
a, b = int(a), int(b)
count = 0
while a <= b:
    count += 1
    a *= 3
    b *= 2

print(count)
