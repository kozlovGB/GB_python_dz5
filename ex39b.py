#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#b)Подумайте как наделить бота ""интеллектом""

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    if x < 1 or 28 < x :
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"{name}, взял {k}, теперь у него {counter}, на столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "bot"
value = 2021
flag = randint(1,2) # флаг очередности
if flag==1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag==1:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = 2
        p_print(player1, k, counter1, value)
    else:
        k = value%29#алгоритм гарантирующий боту победу в случае,если он ходит первый или при ошибке первого ходящего игрока
        counter2 += k
        value -= k
        flag = 1
        p_print(player2, k, counter2, value)

if flag==1:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")