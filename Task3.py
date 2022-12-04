# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import random
from random import randint

def generate_list(number_of_elements):
    result_list = []
    for i in range (number_of_elements):
        result_list.append(randint(1,100) + random())
    return result_list

def find_difference(input_list):
    float_list = []
    for elem in input_list:
        if elem - elem // 1 != 0:
            float_list.append(elem - elem // 1)
    result = round(max(float_list) - min(float_list), 5)
    return result

my_list = generate_list(6)
print(my_list)
print(find_difference(my_list))