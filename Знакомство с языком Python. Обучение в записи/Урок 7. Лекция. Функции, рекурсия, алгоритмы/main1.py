#                                               Задача 1

# Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

def sum_nambers(n): # Опишем функцию и в скобках указываем аргумент который мыхотим передать. Это аргумент (n)
    summa = 0 # Создаем переменую 
    for i in range(1, n+1): # Соотвествено что мы буде делать в нашей фунции. Мы будим идти по циклу for i in range и в скобках указываем (n + 1) так как нам нужно считать сумму.
                            # Но мы помним, что нам сумму нужн считать с первого элемента поэтому записываем так (1, n + 1)
        summa += i  # Также при каждой итерации цикла мы будим увеличивать переменую суммы. Надо ее создать summa и будем ее увеличивать += на нашу переменую i
    # print(summa) # И в этой же функции сразу будем ее выводить

# Теперь нужно ее вызвать
# sum_nambers(5) # Чтобы ее вызвать мы должы написать ее имя sum_namber (и в параметрах передать число (в даном случае 5))

# Запускаем

#  Вывод
#  15
  
# Можно записать еще так
    return summa
# print(sum_nambers(5))

# Запускаем

#  Вывод
#  15

a = sum_nambers(5) # Также можно создать какуето переменую
print(a) #Ивыводим переменую (a)

# Запускаем

#  Вывод
#  15