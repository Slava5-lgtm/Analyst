
from logger import input_data, print_data 



def interface(): 
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - это запись даннх \n 2 - ввывод данных \n ") 

                                               

    command = int(input('Введите число ')) 
    
    # Проверка на правильность ввода
    while command != 1 and command != 2: 
        print("Неправильный ввод") 
        command = int(input('Введите число ')) 

  
    if command == 1: 
        input_data() 
    elif command == 2:
        print_data() 

