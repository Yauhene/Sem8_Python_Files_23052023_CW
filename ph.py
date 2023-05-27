# Прочитать файл

# Распечатать содержимое

# Вывести меню
# - поиск
# - выход
# - вывод всех записей
# - добавить

import os


def readFile(fName):
    with open(fName, 'r', encoding='utf-8') as file:
        fileContent = list()
        for line in file.readlines():
            fileContent.append((list(line.split('\n')[0].split(';'))))
    file.close()
    return fileContent

def prAbonents(abList, currPos=0):
    outStr = ''
    for abStr in range(0, len(abList)):
        for pos in range(0, len(abList[abStr])):
            outStr += abList[abStr][pos] + " "
        if abStr != currPos:
            outStr = '    ' + outStr
        else:
            outStr = '==> ' + outStr
        print(outStr)
        outStr = ''

def findAb(abList):
    getOut = False
    found = list()
    altList = list()
    while getOut != True:
        os.system('CLS')
        arg = input('Введите образец поиска (или Enter для выхода из поиска): ')
        if arg == '':
            getOut = True
            #break
        else:
            arg = arg.lower()
            for ab in abList:
                #---- начинаем хулиганить ----------------
                altStr = ' '.join(ab).lower()
                if altStr.find(arg) != -1:
                    found.append(ab)
            if len(found) > 0:
                print()
                print('========= А вот чего нашлось: ===============')
                print()
                for x in found:
                    for i in x:
                        print(i, ' ', end = '')
                    print()
                print()
                print('1 - редактировать запись,  9 - удалить запись,  "Enter" - выйти из поиска')
                
                choice = input('Ваш выбор: ')
                if choice == '1':
                    print(f'found = {found}')
                    print(f'len(found) = {len(found)}')
                    if len(found) > 1:
                        ab = input('введите порядковый номер абонента (номера указаны в начале записей): ')
                        ab = int(ab)
                        print(f'ab = {ab}')
                    else:
                        print(f'found[0][0] = {found[0][0]}')
                        ab = int(found[0][0])
                        print(f'ab = {ab}')
                        print(f'abList[ab-1] = {abList[ab-1]}')
                        
                    abList[ab-1] = editAb(abList[ab-1], abList)
                    #abList[ab-1] = editAb(abList[ab-1], abList)
                    print(f'abList = {abList}')
                    #saveFile(abList)
                    #input('press!')
                    return abList
                
                if choice == '9':
                    if len(found) > 1:
                        ab = input('введите порядковый номер абонента (номера указаны в начале записей): ')
                        ab = int(ab)
                        #print(f'ab = {ab}')
                    else:
                        #print(f'found[0][0] = {found[0][0]}')
                        ab = int(found[0][0])


            else:
                print()
                print('========= Ничего не найдено ===============')
                print()
                input('Нажмите Enter для продолжения')
        found = list()
    #os.system('CLS')
    return abList

def editAbItem(abPos,itemName, itemStr):
    itemName = int(itemName) 
    print(itemStr)
    print(f'Текущее значение" : {abPos[itemName]}')
    cList=list()
    cList = abPos
    print(f'cList= {cList}')
    new = input('Новое значение" : ')
    abPos[itemName] = new
    print(f'abPos = {abPos}')
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
    choice = int(input('Ваш выбор: '))
    #print(f'choice = {choice}')
    while getOut != True:
        if choice == 1:
            abPos = editAbItem(abPos, 1, 'Фамилия:')
            #print(f'abPos in editAb: {abPos}')
            return abPos
            #break
        if choice == 2:
            abPos = editAbItem(abPos, 2, 'Имя:')
            #print(f'abPos in editAb: {abPos}')
            return abPos
            #break
        if choice == 3:
            abPos = editAbItem(abPos, 3, 'отчество:')
            #print(f'abPos in editAb: {abPos}')
            return abPos
            #break
        if choice == 4:
            abPos = editAbItem(abPos, 4, 'Телефон:')
            #print(f'abPos in editAb: {abPos}')
            return abPos
            #break
        if choice == '':
            getOut = True
    #print(f'Теперь newList = {newList}')
    #input('press!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    return abPos

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

def saveFile(abList, fileName):
    #print('abList из saveFile():')
    #print(abList)
    #print('press***************************')
    tempStr = ''
    with open(fileName, 'w', encoding = 'utf-8') as file:
        for row in abList:
            size = len(row)
            for  i in range(0,size):
                #print(f'i = {i}, size = {size}')
                if i != size-1: 
                    tempStr += row[i] + ';'
                else:
                    tempStr += row[i]

            tempStr += '\n'
            #print(f'tempStr = {tempStr}')
            #input('press!')
        file.write(tempStr)
    file.close()
