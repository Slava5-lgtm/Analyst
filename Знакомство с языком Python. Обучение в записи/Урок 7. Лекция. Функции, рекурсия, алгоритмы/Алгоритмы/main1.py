#                                                       Быстрая сортировка
def quick_sort(array):                                      # Сначала создадим функцию и будем передовать массив (array)
    if len(array) <= 1:                                     # И сразу будем делать проверку если (if) длина нашего массива (len(array)<=1)
        return array                                        # То мы возврашяем этот массив
    else:                                                   # А иначе мы будем выполнять какие небудь действия. У нас повторялись одни и тежи действия можество раз (то есть рекурсия)
         pivot = array[0]                                   # Создаем переменую (pivot) в которой будем сохранять наш первый элемент array[0]
                                                            # Теперь создадим два массива: 
    less = [i for i in array[1:] if i <= pivot]             # В первый массив (less) будем записывать числа которые < нашего значения (array[0]) тоесть (pivot)
                                                            # Будим класть знаения [(i)проходясь по циклу (for i in array[1:(: - воспользуемся срезами) мы будем проходиться по всему
                                                            # элементам и добовлять только те которые будуд <= нашей переменой pivot ])]               
    greater = [i for i in array[1:] if i > pivot]           # Во второй массив (greater) будем записывать числа который > нашего элемента
                                                            # Будим класть знаения [(i)проходясь по циклу (for i in array[1:(: - воспользуемся срезами) мы будем проходиться по всему
                                                            # элементам и добовлять только те которые будуд > нашей переменой pivot ])]"
    # return quick_sort(less) + pivot + quick_sort(greater) Вызываем следущию рекурсию. У нас есть элемент (pivot) и два списка (less и greater). Элемент (pivot) будет находиться 
                                                            # по серидине между этими списками по значеню. Могли бы записать (less + pivot + greater). Но списки (less и greater) не
                                                            # орсортированы. Для них тоже будем вызывать функцию (quick_sort). Будем их сортировать (quick_sort(less) + pivot +
                                                            # + quick_sort(greater)). И соотвествено при первом вызове нашей рекурсии у нас будет возврошяться два неорсортированых
                                                            # списка quick_sort(less) + quick_sort(greater)) и знчения (pivot) которое получено будет точно между этими списками
# print(quick_sort([10, 5, 2, 3]))                          # БУДЕТ ОШИБКА (TypeError: can only concatenate list (not "int") to list) так как нельзя складывать список и числа
                                                            # (quick_sort(less)  quick_sort(greater)) - тип даных список (list), (pivot) - тип даных число (int) 
    return quick_sort(less) + [pivot] + quick_sort(greater) #Здесь мы [pivot] преобразовываем в список (list)
print(quick_sort([10, 5, 2, 3]))