N = int(input())

global_maximum, local_maximum = 0, 0

prev = int(input())

for i in range(1, N):
    num = int(input())

    if local_maximum <= 0:
        local_maximum = num - prev
        temp = i - 1
    else:
        local_maximum = local_maximum + num - prev

    if global_maximum < local_maximum:
        global_maximum = local_maximum
        sell_day = i
        buy_day = temp

    prev = num

print(global_maximum, buy_day + 1, sell_day + 1 if global_maximum > 0 else 0)

# Test data
# 9
# 10
# 2
# 5
# 4
# 9
# 7
# 1
# 6
# 4

# Output
# 7 2 5