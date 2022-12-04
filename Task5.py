# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    else:
        return(fibonacci(number-1) + fibonacci(number-2))

def negafibonacci(number):
    if number == -1:
        return 1
    if number == -2:
        return -1
    else:
        return(negafibonacci(number+2) - negafibonacci(number+1))

def make_fib_list(number):
    list_fib = [0]
    for i in range (1, number + 1):
        list_fib.append(fibonacci(i))
        list_fib.insert(0, negafibonacci(-i))
    return list_fib
        
print(make_fib_list(8))
