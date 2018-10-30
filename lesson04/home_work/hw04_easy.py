# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst_1 = [1, 2, 4, 0]
lst_sq = [a ** 2 for a in lst_1]
print(lst_sq)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst_1 = ["абрикос", "айва", "слива", "СС 20"]
lst_2 = ["айва", "желудь", "банан", "слива"]
sort_list = list (set (lst_1) & set (lst_2))
print(sort_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
count = int (input("Введите количество элементов: ")) #задача из 2-го урока
mylist = []
n = 0
while n < count:
     mylist.append(random.randint(-100, 100))
     n +=1

print(mylist)

sort_list = [el for el in mylist if el % 3 == 0 and el >=0 and el % 4 !=0]
print(sort_list)

