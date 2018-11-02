# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import dir_com_hw05_ez as dc

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
    dc.make_dir(cur_dir)

for cur_dir in dirs:
    dc.del_dir(cur_dir)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import dir_com_hw05_ez as dc

print(dc.dir_list())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import dir_com_hw05_ez as dc

dc.copy_file()