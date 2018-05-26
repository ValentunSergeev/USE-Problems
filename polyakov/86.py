from math import factorial

N = int(input())

odd = [0] * 7
even = [0] * 7

res = 0


def placements(n, k):
    return 0 if n < k else factorial(n) / (factorial(k) * factorial(n-k))


def update_result(i, j, k):
    global res

    if i == j == k:
        res += placements(odd[i], 3) \
               + odd[i] * placements(even[i], 2)
    elif i == j:
        res += placements(odd[i], 2) * odd[k] \
               + placements(even[i], 2) * odd[k] \
               + even[i] * odd[i] * even[k]
    elif j == k:
        res += placements(odd[j], 2) * odd[i] \
               + placements(even[j], 2) * odd[i] \
               + even[j] * odd[j] * even[i]
    elif i == k:
        res += placements(odd[i], 2) * odd[j] \
               + placements(even[i], 2) * odd[j] \
               + even[i] * odd[i] * even[j]
    else:
        res += odd[i] * odd[j] * odd[k] \
               + even[i] * even[j] * odd[k] \
               + even[i] * odd[j] * even[k] \
               + odd[i] * even[j] * even[k]


for i in range(N):
    num = int(input())
    if num % 2 == 0:
        even[num % 7] += 1
    else:
        odd[num % 7] += 1

for i in range(0, 7):
    for j in range(i, 7):
        for k in range(j, 7):
            if (i + j + k) % 7 == 0:
                update_result(i, j, k)

print(int(res))

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
