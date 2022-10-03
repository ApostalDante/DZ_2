""" Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """

n_numbers = int(input("Введите число: "))

def sequence(num):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n_numbers + 1)]   

print(sequence(n_numbers))
print(round(sum(sequence(n_numbers))))

