import os


def get_current_path():
    current_path = os.getcwd()
    return current_path


def check_duplicated_tests(path):
    files_list = []
    tests_list = []
    all_files = os.walk(path)

    for folder, subfolders, files in all_files:
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(folder, filename)
                files_list.append(filename)

        for _ in files_list:
            with open(file_path) as file:
                content = file.readlines()
                for string in content:
                    if string.startswith('def test_'):
                        tests_list.append(string)

    duplicates = list(set([x for x in tests_list if tests_list.count(x) > 1]))
    return duplicates


print(check_duplicated_tests(r'C:\Users\jeykh\OneDrive\Рабочий стол\test'))