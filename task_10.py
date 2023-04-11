from random import randint
"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""
OUTPUT_MESSAGE = 'Минимальное число монеток, которые надо перевернуть - {0}.'
coins = int(input('Enter coins number: '))
coin_list = [randint(0, 1) for i in range(coins)]
count_orel = 0
count_reshka = 0
print(coin_list)
for coin in coin_list:
    if coin == 0:
        count_orel += 1
    else:
        count_reshka += 1
if count_orel > count_reshka:
    print(OUTPUT_MESSAGE.format(count_reshka))
else:
    print(OUTPUT_MESSAGE.format(count_orel))
