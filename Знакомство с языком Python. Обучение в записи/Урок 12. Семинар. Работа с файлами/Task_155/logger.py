
from data_create import name_data, surname_data, phone_data, address_data


# Соотавесвено в это файле logger.py. Создадим две функции

def input_data(): # Функции input_data и пока обозначим как пустым ()
    name = name_data() 
    surname = surname_data() 
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком фрмате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выбирите вариант: "))

        # Проверка на правильность ввода
        
    while var != 1 and var != 2: 
        print("Неправильный ввод") 
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n {surname}\n {phone}\n {address}\n\n")

    elif var == 2:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n") 


def print_data (): # Функции print_data и пока обозначим как пустым ()
    pass

input_data()