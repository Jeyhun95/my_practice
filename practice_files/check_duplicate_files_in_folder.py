# Импортируемт библиотеку для управления ОС
import os

# Создаем два списка, один будет содержать все элементы папки, второй - с заданным расширением
test_files = []
all_files = []

# Парсим элементы в список
for i in os.walk(r"C:\Users\jeykh\OneDrive\Рабочий стол\test"):
    all_files.append(i)

# Перебираем элементы и добавляем в новый список только с заданным расширением
for i in all_files:
    for j in i:
        for h in j:
            if h.endswith('.py'):
                test_files.append(h)

# Создаем список с дубликатами и принтим его
duplicates = list(set([x for x in test_files if test_files.count(x) > 1]))
print(duplicates)
