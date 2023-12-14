file = open(r'C:\Users\jeykh\OneDrive\Рабочий стол\test\my_file.txt', encoding='utf-8')

test = file.readlines()

duplicated_tests = []

for i in test:
    if i.startswith('def test_'):
        duplicated_tests.append(i)

print(duplicated_tests)
