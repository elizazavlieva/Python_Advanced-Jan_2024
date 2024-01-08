numbers = [int(i) for i in input().split()]
n = numbers[0]
m = numbers[1]
n_set = set()
m_set = set()
for i in range(n + m):
    num = int(input())
    if i < n:
        n_set.add(num)
    else:
        m_set.add(num)

unique_num = n_set.intersection(m_set)
for i in unique_num:
    print(i)
