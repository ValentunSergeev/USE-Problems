N = int(input())

nechet = [0] * 7
chet = [0] * 7

res = 0

def cnt(i, j, k):
    global res

    if i == j == k:
        res += nechet[i] * (nechet[i] - 1) * (nechet[i] - 2) \
               + nechet[i] * chet[i] * (chet[i] - 1)
    elif i == j:
        res += nechet[i] * (nechet[i] - 1) * nechet[k]\
               + chet[i] * (chet[i] - 1) * nechet[k]\
               + chet[i] * nechet[i] * chet[k]
    elif j == k:
        res += nechet[j] * (nechet[j] - 1) * nechet[i]\
               + chet[j] * (chet[j] - 1) * nechet[i]\
               + chet[j] * nechet[j] * chet[i]
    elif i == k:
        res += nechet[i] * (nechet[i] - 1) * nechet[j]\
               + chet[i] * (chet[i] - 1) * nechet[j]\
               + chet[i] * nechet[i] * chet[j]
    else:
        res += nechet[i] * nechet[j] * nechet[k]\
               + chet[i] * chet[j] * nechet[k]\
               + chet[i] * nechet[j] * chet[k]\
               + nechet[i] * chet[j] * chet[k]


for i in range(N):
    num = int(input())
    if num % 2 == 0:
        chet[num % 7] += 1
    else:
        nechet[num % 7] += 1

for i in range(0, 7):
    for j in range(i, 7):
        for k in range(j, 7):
            if (i + j + k) % 7 == 0:
                cnt(i, j, k)

print(res)

# Test data
# 7
# 8
# 11
# 14
# 15
# 2
# 4
# 7
# Output
# 2