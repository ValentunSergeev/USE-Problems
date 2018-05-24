N = int(input())

p_1, p_2 = 1, 1

result = 1

global_max = 0

last_negative = 0


def normalize_result():
    global p_1, p_2, result

    if result < 0:
        if p_2 > 0:
            p_2 = result // p_1 * last_negative

        result //= max(p_1, p_2)


for i in range(N):
    num = int(input())

    if num != 0:
        result *= num

    if num > 0:
        if last_negative < 0:
            p_2 *= num
        else:
            p_1 *= num
    elif num < 0:
        if last_negative < 0:
            p_2 = num
        else:
            p_1 *= num
        last_negative = num
    else:
        normalize_result()
        global_max = max(result, global_max)

        p_1, p_2 = 1, 1

        is_negative_met = False
        result = 1

normalize_result()
global_max = max(global_max, result)

print(global_max)
# Test data
# 7
# 2
# 3
# -2
# -3
# -1
# 4
# 6
# Output
# 72

