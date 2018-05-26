max_dist = 4  # менне, чем на 5

N = int(input())
m_26, m_13, m_even, m_odd = 0, 0, 0, 0

result = 0
queue = []


# Пересчет делителей - либо увеличение(при добавлении числа), либо уменьшение(при удалении)
def change_m(num, delete):
    delta = -1 if delete else 1

    global m_26, m_13, m_even, m_odd

    if num % 26 == 0:
        m_26 += delta
    elif num % 13 == 0:
        m_13 += delta
    elif num % 2 == 0:
        m_even += delta
    else:
        m_odd += delta


# Начальное заполнение очереди
for i in range(max_dist):
    num = int(input())
    queue.append(num)

    change_m(num, False)

for i in range(max_dist, N):
    num = int(input())

    # Считаем пары
    if num % 26 == 0:
        result += m_odd + m_13
    elif num % 13 == 0:
        result += m_26 + m_even
    elif num % 2 == 0:
        result += m_13
    else:
        result += m_26

    # Двигаем очередь вправо
    deleted = queue.pop(0)
    change_m(deleted, True)

    queue.append(num)
    change_m(num, False)

print(result)

# Test data
# 7
# 4
# 14
# 27
# 33
# 7
# 2
# 13
# Output
# 1
