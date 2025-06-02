# codeforces: https://codeforces.com/problemset/problem/339/A

x = input()
x = x.split("+")
x = [int(v) for v in x]

def mergeSort(a, s, e):
    if s < e:
        m = s+(e-s)//2
        mergeSort(a, s, m)
        mergeSort(a, m+1, e)
        merge(a, s, m, e)

def merge(a, s, m, e):
    n1 = m - s + 1
    n2 = e - m

    S = [0] * n1
    E = [0] * n2

    for i in range(0, n1):
        S[i] = a[s + i]
    for j in range(0, n2):
        E[j] = a[m + 1 + j]
    
    i = 0
    j = 0
    k = s

    while i < n1 and j < n2:
        if S[i] <= E[j]:
            a[k] = S[i]
            i += 1
        else:
            a[k] = E[j]
            j += 1
        
        k += 1
    
    while i < n1:
        a[k] = S[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = E[j]
        j += 1
        k += 1
    

mergeSort(x, 0, len(x)-1)
result = ""
for c in x:
    result+=f"{c}+"

print(result.strip("+"))


