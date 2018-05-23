N = int(input())

odd = [0] * 7
even = [0] * 7

res = 0


def update_result(i, j, k):
    global res

    if i == j == k:
        res += odd[i] * (odd[i] - 1) * (odd[i] - 2) \
               + odd[i] * even[i] * (even[i] - 1)
    elif i == j:
        res += odd[i] * (odd[i] - 1) * odd[k] \
               + even[i] * (even[i] - 1) * odd[k] \
               + even[i] * odd[i] * even[k]
    elif j == k:
        res += odd[j] * (odd[j] - 1) * odd[i] \
               + even[j] * (even[j] - 1) * odd[i] \
               + even[j] * odd[j] * even[i]
    elif i == k:
        res += odd[i] * (odd[i] - 1) * odd[j] \
               + even[i] * (even[i] - 1) * odd[j] \
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
