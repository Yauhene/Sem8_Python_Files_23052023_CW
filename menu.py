from ph import *

def mainMenu():
    getOut=False
    while getOut != True:
        print('==================================================')
        print('Выберите пункт меню, нажав соответствующую цифру и Enter. ')
        print('1. Найти абонента')
        print('2. Вывести полный список абонентов')
        print('3. Добавить нового абонента')
        print('Q/q - Выйти из программы')
        choice = input('Ваш выбор: ')
        choice = choice.lower()
        if choice == 'Q' or choice == 'q' or choice == 'й' or choice == 'Й':
            getOut = True
            print()
            print('Дело хозяйское... До новых встреч!')
            print()
        if choice == '1':
            print(findAb(readFile('phones.txt')))