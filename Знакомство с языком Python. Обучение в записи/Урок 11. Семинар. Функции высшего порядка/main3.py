
#                                                           Задача №3.

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если
# значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая
# принимает объект и вычисляет его характеристику.

# Ввод:                                                                                                                 Вывод:

# values = [0, 2, 10, 6] - Есть список                                                                                  same
# if same_by(lambda x: x % 2, values): - делаем проверку. Наше функсия (same_by) возвращают True либо  False 
#   print(‘same’) - Если наша функция четная ввыводим  (‘same’) 
# else:
# print(‘different’) - А иначе ввыводим (‘different’)

def same_by (characteristic, objects): # Напишем функцию (same_by)
    result = True # Создадим переменую в которой будим хранить результат работы нашей функции. Это либо True, либо False
    list1 = [characteristic(x) for x in objects] # Создадим список (list1) [в котором каждый элемент будет результат работы нашей функции к нашему списку. Мы берем нашу функцию
                                                 # (characteristic применяем к обекту (х)) этот (х) у нас берется из цикла ( for x in objects) ]
    for i in range(len(list1) - 1): #  Сооздаем цикл (for i in range (где пройдемся по всему нашему спмску (len(list1) за исключением последнего элемента (-1))))
        if list1[i] != list1[i+1]: # Если (if) наш list1[i] не равно (!=) list1[i+1]
            result = False # То результат равен False
    return result  # По завершению работы нашего цикла (return) возрошяем результат (result)

values = [1, 3, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

