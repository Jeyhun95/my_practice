
file = open(r'/Users/seyfme/PycharmProjects/folder/1.py', encoding='utf-8')

test = file.readlines()

duplicated_tests = []

for i in test:
    if i.startswith('def test_'):
        duplicated_tests.append(i)

print(duplicated_tests)
