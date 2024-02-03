import os


def extensions(dir_name, first_level=False):
    for file in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file)

        if os.path.isdir(file_path) and not first_level:
            extensions(file_path, first_level=True)
        elif os.path.isfile(file_path):
            extension = os.path.splitext(file)
            directory_info[extension[-1]] = directory_info.get(extension[1], []) + [file]


path = os.path.join('Resources')
directory_info = {}

try:
    extensions(path)
except FileNotFoundError:
    print('File is not found!')
else:
    sorted_info = sorted(directory_info.items(), key=lambda kvp: kvp[0])

    result = []
    for file_type, files in sorted_info:
        result.append(file_type)

        for file_ in files:
            result.append(f'- - - {file_}')

    result_path = os.path.join('text_folder', 'report.txt')
    with open(result_path, "a") as report:
        report.write("\n".join(result))
