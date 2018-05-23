minimal_dist = 5

N = int(input())
m_26, m_13, m_even, m_odd = 0, 0, 0, 0

# Очередь из пяти элементов, с начала в ней первые 5 чисел, затем она сдвигается вправо:
# удаляется первый, добалвяется шестой и т.д.
queue = [int(input()) for i in range(minimal_dist)]

result = 0

for i in range(minimal_dist, N):
    # Новый елемент, с которым можно образовывать пары
    first = queue[0]

    # пересчитываем досутпное для формирования пар распределение чисел по делителям
    if first % 26 == 0:
        m_26 += 1
    elif first % 13 == 0:
        m_13 += 1
    elif first % 2 == 0:
        m_even += 1
    else:
        m_odd += 1

    #  Новое число
    num = int(input())

    # Формируем пары, увеличиваем счетчик
    if num % 26 == 0:
        result += m_odd + m_13
    elif num % 13 == 0:
        result += m_26 + m_even
    elif num % 2 == 0:
        result += m_13
    else:
        result += m_26

    # Сдвигаем очередь
    queue.pop(0)
    queue.append(num)

print(result)

# Test data
# 7
# 4
# 14
# 27
# 39
# 7
# 2
# 13
# Output
# 2


