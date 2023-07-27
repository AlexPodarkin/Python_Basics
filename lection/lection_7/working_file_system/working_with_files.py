# Работа с файлами
import os
from pathlib import Path
import shutil

# print("Переименование файлов")
# os.rename('old_name.py', 'new_name.py')
# p = Path('old_file.py')
# p.rename('new_file.py')
# Path('new_file.py').rename('newest_file.py')

# print("Перемещение файлов")
# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
#
# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# print("Копирование файлов")
# shutil.copy('one.txt', 'dir')
# shutil.copy2('two.txt', 'dir')
# print("Если стоит задача скопировать каталог ")
# shutil.copytree('dir', 'more_dir')

# print("Удаление файлов")
# shutil.rmtree('dir')

print("Если же необходимо удалить один файл")
# os.remove('one_more_dir/one.txt')
# Path('one_more_dir/one_more.txt').unlink()
