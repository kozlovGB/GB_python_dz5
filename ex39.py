#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#Формула для нахождения нужного числа конфет: x%(m+1),
#где x-исходное колличество конфет, m-количество конфет, которые можно взять за один ход.

print("Первому игроку необходимо взять:", 2021%(28+1),'конфет')