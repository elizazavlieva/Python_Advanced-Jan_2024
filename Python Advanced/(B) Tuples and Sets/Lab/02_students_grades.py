n = int(input())
student_info = {}
for _ in range(n):
    name, grades = input().split()
    if name not in student_info:
        student_info[name] = []
    student_info[name].append(float(grades))

for k, v in student_info.items():
    grade = " ".join([f'{i:.2f}' for i in v])
    print(f'{k} -> {grade} '
          f'(avg: {sum(v) / len(v):.2f})')
