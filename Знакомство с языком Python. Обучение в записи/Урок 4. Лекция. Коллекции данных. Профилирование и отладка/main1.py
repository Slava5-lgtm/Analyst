#                                                    Списки

# Список - это упорядоченный конечный набор элементов. Давайте разбираться, по сути список - это тот же самый массив, в котором можно хранить элементы любых типов данных.
# Как работать со списками?

list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_3 = [7, 9, 11, 13, 15, 17]

# В списках существует нумерация, которая начинается с 0, чтобы вывести первый элемент списка воспользуемся следующей конструкцией:

print(list_1) 
print(list_2)
print(list_3) # [7, 9, 11, 13, 15, 17]
print(*list_3) # * ставим чтобы небыло скобрк 7 9 11 13 15 17 