N = int(input())

a1, a2 = int(input()), int(input())
global_maximum, local_maximum = a2 - a1, a2 - a1

prev = a2

for i in range(N - 2):
    num = int(input())

    local_maximum = max(0, local_maximum) + num - prev
    global_maximum = max(local_maximum, global_maximum)

    prev = num

print(global_maximum if global_maximum > 0 else 0)

# Test data
# 9
# 10
# 2
# 5
# 4
# 8
# 7
# 1
# 6
# 4
# Output
# 6