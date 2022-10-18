# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# print('Задача 1. Сумма элементов нечетных позиций')
# print('Введите числа через пробел')
# list1 = list (map(int, input().split()))

# sum_elements = 0

# for i in range(1, len(list1), 2):
#     sum_elements += list1[i]
    
# print('Сумма элементов нечетных позиций = ', end='')
# print(f'{sum_elements}') 

# print()
# print()   

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# print('Задача 2. Произведение пар чисел списка')
# from random import randint

# number = int(input('Введите размер списка '))
# list1 = []
# list2 = []

# for i in range(number):
#     list1.append(randint(0, 9))

# for j in range((len(list1) + 1) // 2):
#     list2.append(list1[j] * list1[-(j + 1)])
        
# print(f'Исходный список {list1}')
# print(f'Произведение пар чисел списка {list2}')

# print()
# print()

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform


n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):
    
    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif,2))