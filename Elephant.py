# codeforces: https://codeforces.com/problemset/problem/617/A

# - 1
x = int(input())
count = x // 5 + (1 if x % 5 != 0 else 0)
print(count)

# - 2
# x = int(input())
# e = 0
# count = 0
# while e != x:
#     d = x - e
#     if d < 5:
#         if d < 4:
#             if d < 3:
#                 if d < 2:
#                     e += 1
#                 else:
#                     e += 2
#             else:
#                 e += 3
#         else:
#             e += 4
#     else:
#         e += 5

#     count += 1

# print(count)