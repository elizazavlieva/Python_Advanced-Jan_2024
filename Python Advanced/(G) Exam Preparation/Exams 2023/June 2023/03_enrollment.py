def gather_credits(needed_credits, *args):
    courses = []
    reached_credits = 0
    for course, credits in args:
        if reached_credits >= needed_credits:
            break
        if course in courses:
            continue
        courses.append(course)
        reached_credits += credits
    if reached_credits < needed_credits:
        return f'You need to enroll in more courses! ' \
               f'You have to gather {needed_credits - reached_credits} credits more.'
    return f'Enrollment finished! Maximum credits: {reached_credits}.\n' \
           f'Courses: {", ".join(sorted(courses))}'

'''TESTS'''

print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),

))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

