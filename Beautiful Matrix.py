# codeforce: https://codeforces.com/problemset/problem/263/A

one_location = ()
for i in range(5):
    m = input().split()
    if '1' in m:
        one_location = (i, m.index('1'))

# center = (3, 3)
y = 2 - one_location[0]
x = 2 - one_location[1]

# |x| and |y|
if y < 0:
    y = -1 * y
if x < 0:
    x = -1 * x

print(x+y)