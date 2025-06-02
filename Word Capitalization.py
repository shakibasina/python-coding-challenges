# codeforces: https://codeforces.com/problemset/problem/281/A

# - 1 :)))
# s = input()
# print(s.capitalize())

# - 2
# s = input()
# print(s[0].upper()+s[1:])

# - 3
import string

s = input()
lower_to_upper = {letter: letter.upper() for letter in string.ascii_lowercase}
if s[0] in lower_to_upper:
    print(lower_to_upper[s[0]]+s[1:])
else:
    print(s)
