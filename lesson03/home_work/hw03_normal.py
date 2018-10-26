# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(8, 13)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    print (origin_list)
    lst = []
    while len(origin_list) > 0 :
        a = origin_list[0]
        for i in origin_list :
            if i <= a :
                a = i
        origin_list.remove(a)
        lst.append(a)
    print (lst)



sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, itr):

    new_itr = [elem for elem in itr if func(elem)]
    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)
    print(new_itr)
    return new_itr

#фильтр - возвращает значения,больше указанного в условии
my_filter(lambda i: i > 3, {2, 10, -13, 7.5, 20, -11, 40, 40, 0})





# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parral(a1,a2,a3,a4):
    def centerpoint(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if a1 == a3: return False
    return centerpoint(a1,a3) == centerpoint(a2,a4)

#проверяем равенство