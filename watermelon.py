# codeforces: https://codeforces.com/problemset/problem/4/A

try:
    n = float(input())
    if n != 2 and n % 2 == 0:
        print("YES")
    else:
        print("NO")
except:
    print("NO")
