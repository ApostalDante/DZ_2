""" Реализуйте алгоритм перемешивания списка. """

import random

def get_list(n, left, right):
    return [random.randint(left, right) for i in range(n)]

def shuffle(lst):
    return random.shuffle(lst)

num = 10
left = -10
right = 20

list = get_list(num, left, right)
print(list)
shuffle(list)
print(list)