N = int(input())

first = int(input())
global_maximum, local_maximum = first, first

for i in range(N - 1):
    num = int(input())

    local_maximum = max(num, num + local_maximum)
    global_maximum = max(global_maximum, local_maximum)

print(global_maximum)

# Test Data
# 9
# -2
# 1
# -3
# 4
# -1
# 2
# 1
# -5
# 4

# Output
# 6