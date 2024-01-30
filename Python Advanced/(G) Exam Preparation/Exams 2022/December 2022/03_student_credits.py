def students_credits(*args):
    student_info = {}

    for element in args:

        course = element.split('-')
        course_name = course[0]
        credit = int(course[1])
        max_points = int(course[2])
        student_points = int(course[3])
        try:
            student_credits = credit / (max_points/student_points)
        except ZeroDivisionError:
            student_credits = 0

        student_info[course_name] = student_credits

    result = []
    if 240 <= sum(student_info.values()):

        result.append(f'Diyan gets a diploma with {sum(student_info.values()):.1f} credits.')
    else:

        result.append(f'Diyan needs {(240 - sum(student_info.values())):.1f} credits more for a diploma.')

    sorted_info = sorted(student_info.items(), key=lambda kvp: (-kvp[1]))

    for course_n, d_credits in sorted_info:
        result.append(f"{course_n} - {d_credits:.1f}")

    return "\n".join(result)


'''TESTS'''
print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
