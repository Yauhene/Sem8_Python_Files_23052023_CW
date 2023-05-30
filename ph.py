import os

# функция чтения файла в список, каждый элемент списка - список данных
def readFile(fName):
    with open(fName, 'r', encoding='utf-8') as file:
        fileContent = list()
        for line in file.readlines():
            fileContent.append((list(line.split('\n')[0].split(';'))))
    file.close()
    return fileContent

# функция вывода списка обонентов в консоль, вывод всегда находится над опциями гл. меню
def prAbonents(abList, currPos=0):
    outStr = ''
    for abStr in range(0, len(abList)):
        if abList[abStr][0] != '':
            for pos in range(0, len(abList[abStr])):
                outStr += abList[abStr][pos] + " "
            if abStr != currPos:
                outStr = '    ' + outStr
            else:
                outStr = '==> ' + outStr
            print(outStr)
            outStr = '' 

# функция поиска абонента по фрагментам информации,
# поиск идет сразу по всем полям записи
def findAb(abList):
    getOut = False # флаг выхода из цикла меню
    found = list() # список результатов текстового поиска
    
    while getOut != True:
        os.system('CLS')
        arg = input('Введите образец поиска (или Enter для выхода из поиска): ')
        if arg == '':
            getOut = True
        else:
            arg = arg.lower()
            for ab in abList:
                altStr = ' '.join(ab).lower()
                if altStr.find(arg) != -1:
                    found.append(ab)
            if len(found) > 0:
                print()
                print('========= А вот чего нашлось: ===============')
                print()
                print('ID:')
                for x in found:
                    for i in x:
                        print(i, ' ', end = '')
                    print()
                print()
                print('1 - редактировать запись,  9 - удалить запись,  "Enter" - выйти из поиска')
                
                choice = input('Ваш выбор: ')
                if choice == '1':
                    if len(found) > 1:
                        ab = input('введите ID абонента (номера указаны в начале записей): ')
                        ab = int(ab)
                        print(f'ab = {ab}')
                    else:
                        ab = int(found[0][0])
                    print()    

                    abList[ab-1] = editAb(abList[ab-1], abList)
                    return abList
                
                if choice == '9':
                    print()
                    if len(found) > 1:
                        ab = input('введите ID абонента (номера указаны в начале записей): ')
                        print()
                        ab = int(ab)
                    else:
                        ab = int(found[0][0])
                    print('Вы уверены, что хотите удалить эту запись?')
                    print()

                
                    for x in abList[ab-1]:
                        print(x, ' ', end = '')
                    print()
                    print()
                    delYes = input('Введите "y" (Yes) для подтверждения удаления либо "Enter": ')
                    if delYes == 'Y' or delYes == 'y' or delYes == 'н' or delYes == 'Н':
                        for vol in range(0, len(abList[ab-1])):
                            abList[ab-1][vol] = ''
                        print('... мир праху его.')

                if choice == '':
                    getOut = True

            else:
                print()
                print('========= Ничего не найдено ===============')
                print()
                input('Нажмите Enter для продолжения')
        found = list()
    #os.system('CLS')
    return abList

# подфункция редактирования записи
def editAbItem(abPos,itemName, itemStr):
    itemName = int(itemName) 
    print(itemStr)
    print(f'Текущее значение" : {abPos[itemName]}')
    cList=list()
    cList = abPos
    new = input('Новое значение" : ')
    abPos[itemName] = new
    return abPos

def editAb(abPos,fileData):
    getOut = False
    newList = list(abPos)
    
    print()
    print('Что бы Вы хотели изменить? Введите соответствующую цифру: ')
    print('1 - фамилию ')
    print('2 - имя')
    print('3 - отчество')
    print('4 - номер телефона')
    print('"Enter" - выход из редактирования')
    choice = input('Ваш выбор: ')
    while getOut != True:
        if choice == '1':
            abPos = editAbItem(abPos, 1, 'Фамилия:')
            return abPos
        if choice == '2':
            abPos = editAbItem(abPos, 2, 'Имя:')
            return abPos
        if choice == '3':
            abPos = editAbItem(abPos, 3, 'отчество:')
            return abPos
        if choice == '4':
            abPos = editAbItem(abPos, 4, 'Телефон:')
            return abPos
        if choice == '':
            getOut = True

    return abPos

# функция добавления записи абонента
def addAb(abList):
    tempList = list()
    getOut = False
    while getOut != True:
        newAbLastName = input('Введите фамилию абонента:  ')
        newAbName = input('Введите имя абонента:      ')
        newAbByDad = input('Введите отчество абонента: ')
        newAbPhone = input('Введите номер телефона:    ')
        print('---------')
        choice = input("Все верно? Для сохранения нажмите 'Y', для редактирования 'N' и Enter: ")
        if choice == 'y' or choice == 'Y' or choice == 'н' or choice == 'Н':
            
            tempList.append(str(len(abList)+1))
            tempList.append(newAbLastName)
            tempList.append(newAbName)
            tempList.append(newAbByDad)
            tempList.append(newAbPhone)
            abList.append(tempList)
            getOut = True

    tempStr = ', '.join(tempList)
    return abList

# функция сохранения данных из списка в файл
# нумерация записей абонентов корректируется для компесации удалений абонентов
def saveFile(abList, fileName):
    tempStr = ''
    with open(fileName, 'w', encoding = 'utf-8') as file:
        counter = 1
        for row in abList:
            size = len(row)
            if row[0] != '':
                tempStr += str(counter) + ';'
                for i in range(1,size):                        
                    if i != size-1: 
                        tempStr += row[i] + ';'
                    else: 
                        tempStr += row[i]
                tempStr += '\n'
                
                print()
            
                counter += 1
             
        file.write(tempStr)
    file.close()
