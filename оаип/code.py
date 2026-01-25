import os
file_path='zapiska.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('йоу \n')
    file.write('работа с файлами. \n')
if os.path.exists(file_path):
    print("фай создан:", file_path)

with open(file_path, 'a', encoding='utf-8') as file:
    file.write("добавленная строка 1\n")
    file.write("добавленная строка 2\n")
print("текст добавлен")

print("\n содержимое файла:")
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

os.system(f'notepad {file_path}')