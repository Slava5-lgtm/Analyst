#                                                               Задача №2.

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше
# данного. Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод:                                      Ввод:
# 5                                          5
# 1 2 3 4 5                                  1 5 1 5 1
# Вывод:                                     Вывод:
# 0                                          2

# (каждое число вводится с новой строки)

n = int(input(' Введите количесво элементов массива '))
list1 = list() # Создаем список
for i in range(n): # При помощи цикла заполняем элементами
    x = int(input(' Введите числа '))
    list1.append(x) # Добовлчем в список

count = 0 # Создодим переменую счетчик. Для того чтобы могли считать сколько элементов подходит под наше условия
for i in range(1, n-1): # Создодим цикл. Но здесь укажем другой диапзон от 1 до n - 1 элемента. Такой деапозон пишем чтобы правильно сравнивались числа
    if list1[i-1] < list1[i]  > list1[i+1]: # если (if) наш i минус первый элемент меньше чем i элемент и (and) одновремено с этим i > чем i + 1
    # Записать можно и так if list1[i-1] < list1[i] and list1[i] > list1[i+1] 
                                    # Если это так 
        count +=1 # Нашу переменую count увеличиваем на единицу
print(count)