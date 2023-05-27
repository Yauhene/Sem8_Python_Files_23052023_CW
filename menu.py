from ph import *
import os

def mainMenu(fileContent, pos):

    tempList = list()
    
    getOut=False
    while getOut != True:
        os.system('CLS')
        #fileContent = readFile('phones.txt')
        prAbonents(fileContent)
        
        print('==================================================')
        print('Выберите пункт меню, нажав соответствующую цифру и Enter. ')
        print('1. Найти абонента/Изменить запись/Удалить абонента')
        print('2. Вывести полный список абонентов')
        print('3. Добавить нового абонента')
        print('4. Сохранить изменения')
        print('Q/q - Выйти из программы')
        choice = input('Ваш выбор: ')
        choice = choice.lower()
        if choice == 'Q' or choice == 'q' or choice == 'й' or choice == 'Й':
            getOut = True
            saveFile(fileContent,'phones.txt')
            print()
            print('Дело хозяйское... До новых встреч!')
            print()
        if choice == '1':
            #findAb(readFile('phones.txt'))
            fileContent = findAb(fileContent)
            #print(f'fileContent после изменения:')
            #print(fileContent)
        if choice == '2':
            prAbonents(readFile('phones.txt'))

        if choice == '3':
            fileContent = addAb(readFile('phones.txt'))

        if choice == '4':
            saveFile(fileContent, 'phones.txt')

        if choice == 'u' or choice == 'г':
            if pos != 0:
                pos = pos - 1
                prAbonents(fileContent, pos)
        if choice == 'd' or choice == 'в':
            if pos != len(fileContent)-1:
                pos = pos + 1
                prAbonents(fileContent, pos)
    return fileContent    
            
            