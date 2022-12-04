# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


def multiply_couples(input_list):
    result_list = []
    if len(input_list) % 2 == 0:
        limit = len(input_list) // 2
    else: 
        limit = len(input_list) // 2 + 1
    for i in range (limit):
        result_list.append(input_list[i] * input_list[len(input_list) - i -1])
    return result_list

print(multiply_couples([2, 3, 5, 6]))

        
