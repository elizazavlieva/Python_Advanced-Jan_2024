def softuni_students(*args, **kwargs):
    students_data = {}
    invalid_users = set()

    for id, username in args:
        if id in kwargs.keys() and username not in students_data:
            students_data[username] = kwargs[id]
        else:
            invalid_users.add(username)
    result = ''
    sorted_data = sorted(students_data.items())
    for student, courses in sorted_data:
        result += f"*** A student with the username {student} " \
                      f"has successfully finished the course {courses}!\n"
    if invalid_users:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_users))}"

    return result


'''TESTS'''

print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
