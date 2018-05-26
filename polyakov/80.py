N = int(input())

m_26, m_13, m_even, m_odd = 0, 0, 0, 0

# Считаем количство чисел, делящихся на 26, 13, 2 и нечётных.
for i in range(N):
    num = int(input())

    if num % 26 == 0:
        m_26 += 1
    elif num % 13 == 0:
        m_13 += 1
    elif num % 2 == 0:
        m_even += 1
    else:
        m_odd += 1

# Считаем количество подходящих пар: 26 и нечётные, 13 и 26, 13 и чётные
result = m_26 * m_odd + m_13 * m_even + m_26 * m_13

print(result)

# Test data:
# 5
# 4
# 13
# 27
# 39
# 7
# Output
# 2