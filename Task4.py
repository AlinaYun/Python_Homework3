# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def from_dec_to_bin (decimal_number):
    result = ""
    while decimal_number > 0:
        result += str(decimal_number - decimal_number // 2 * 2)
        decimal_number //= 2
    return result[::-1]

print(from_dec_to_bin(45))