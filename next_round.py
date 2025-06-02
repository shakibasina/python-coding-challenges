# codeforces: https://codeforces.com/problemset/problem/158/A

n, k = input().split(" ")
n, k = int(n), int(k)

scores = input().strip().split(" ")
k_score = int(scores[k-1])
next_round_count = 0
for score in scores:
    if int(score) > 0 and int(score) >= k_score:
        next_round_count += 1

print(next_round_count)