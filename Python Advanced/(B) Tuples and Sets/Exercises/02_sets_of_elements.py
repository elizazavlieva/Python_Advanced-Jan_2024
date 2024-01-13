n, m = [int(i) for i in input().split()]
n_set = set(int(input()) for i in range(n+m) if i <= n)
m_set = set(int(input()) for i in range(n+m) if i > n)

for i in n_set.intersection(m_set):
    print(i)