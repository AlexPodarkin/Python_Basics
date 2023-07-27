# Работа с файловой системой
import os
from pathlib import Path
import shutil

print("\nзапрос текущей рабочей директории из 2-х самых популярных библиотек")
print(os.getcwd())
print(Path.cwd())

print("изменение рабочей директории")
# os.chdir("../..")

print("Создание каталогов")
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

print("А если необходимо создать несколько вложенных друг в друга каталогов, код будет следующим:")
# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

print("\nУдаление каталогов(Удалить можно лишь пустой каталог)")
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

print("Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и файлы),"
      " подойдёт функция из модуля shutil")
# shutil.rmtree('dir')
# shutil.rmtree('some_dir')

print("Формирование пути ")
# В операционной системе Windows для указания пути используется обратный слеш \.
# В Unix системах путь разделяется слешем. Чтобы программа работала одинаково на
# любой ОС рекомендуется использовать специальную функцию join из os.path для
# склеивания путей.
file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
