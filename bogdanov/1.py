N = int(input())
CENTRAL = 1

sum_central, sum_central_no = 0, 0
is_central_available = True

for i in range(N):
    nums = [int(s) for s in input().split()]

    max1 = max(nums)

    if nums.index(max1) == CENTRAL:
        max2 = max(nums[0], nums[2])

        if is_central_available:
            sum_central_no += max1
            sum_central += max2
            is_central_available = False
        else:
            if sum_central_no + max2 >= sum_central + max1:
                is_central_available = True
                sum_central_no, sum_central = sum_central_no + max2, sum_central_no + max2
            else:
                is_central_available = False
                temp = sum_central_no
                sum_central_no = sum_central + max1
                sum_central = temp + max2

    else:
        sum_central += max1
        sum_central_no += max1

print(max(sum_central, sum_central_no))