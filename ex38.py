#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt_start = input("Введите текст через пробел:\n")
print("Исходный текст:", txt_start)
txt_finish=filter(lambda x: "абв" not in  x.lower(), txt_start.split())
print("Конечный конечный текст:\n",*txt_finish)