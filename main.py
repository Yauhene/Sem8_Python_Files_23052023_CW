from ph import *
from menu import *
import os

os.system('CLS') # очистка консоли
currPose = 0


fileContent = readFile('phones.txt') #чтение файла-хранилища в память

saveFile(fileContent, 'phones.bak') #создание bak-файла

mainMenu(fileContent, currPose)

