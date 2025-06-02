# codeforces: https://codeforces.com/problemset/problem/236/A

s = input()
count = len({c for c in s})
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")