import os

root_path = r'/Users/seyfme/PycharmProjects/folder'
files_list = []
tests_list = []
duplicates = []

all_files = os.walk(root_path)

for folder, subfolders, files in os.walk(root_path):
    for filename in files:
        if filename.endswith(".py"):
            file_path = os.path.join(folder, filename)
            files_list.append(filename)
    for file in files_list:
        with open(file_path) as file:
            content = file.readlines()
            for string in content:
                if string.startswith('def test_'):
                    tests_list.append(string)

duplicates = list(set([x for x in tests_list if tests_list.count(x) > 1]))

print(duplicates)