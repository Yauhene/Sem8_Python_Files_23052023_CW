from ph import *
from menu import *
import os

# spis = ["123", "324"]
# data = open('test.txt', 'w')
# data.writelines(spis)

os.system('CLS') # очистка консоли
currPose = 0
fileContent = readFile('phones.txt')
saveFile(fileContent, 'phones.bak')
#prAbonents(fileContent)
mainMenu(fileContent, currPose)
#fileContent = mainMenu(fileContent, currPose)
# print('В итоге fileContent: ')
# print(fileContent)