# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def generate_list(number_of_elements):
    result_list = []
    for i in range (number_of_elements):
        result_list.append(randint(0, 100))
    return result_list

def sum_odd_index(input_list):
    result = 0
    for i in range (1, len(input_list), 2):
        result += input_list[i]
    return result

number_of_elements = int(input("Введите число элементов в списке: "))
my_list = generate_list(number_of_elements)
print(my_list)
print (sum_odd_index(my_list))