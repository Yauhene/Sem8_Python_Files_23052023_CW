# Прочитать файл

# Распечатать содержимое

# Вывести меню
# - поиск
# - выход
# - вывод всех записей
# - добавить

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

def findAb(findArg):
    getOut = False
    found = list()
    while getOut != True:
        arg = input('Введите образец поиска: ')
        if arg == '':
            getOut = True
        else:
            arg = arg.lower()
            for ab in findArg:
                if ab[1].lower().find(arg) != -1:
                    found.append(ab)
            if len(found) > 0:
                print()
                print('========= А вот чего нашлось: ===============')
                print()
            for x in found:
                for i in x:
                    print(i, ' ', end = '')
                print()
    return found
