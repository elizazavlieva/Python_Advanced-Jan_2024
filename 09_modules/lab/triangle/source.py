def print_triangle(n):
    result = []
    for i in range(2, n + 2):
        current = [j for j in range(1, i)]
        result.append(current)
    for k in range(n - 1, 0, -1):
        current = [l for l in range(1, k + 1)]
        result.append(current)

    print("\n".join([" ".join(map(str, el)) for el in result]))
