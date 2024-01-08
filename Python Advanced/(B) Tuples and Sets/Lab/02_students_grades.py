n = int(input())
student_info = {}
for _ in range(n):
    name, grades = input().split()
    if name not in student_info:
        student_info[name] = []
    student_info[name].append(float(grades))

for k, v in student_info.items():
    avg_grade = sum(v) / len(v)
    print(f'{k} ->', end="")
    for grade in v:
        print(f' {grade:.2f}', end="")
    print(f' (avg: {avg_grade:.2f})')
