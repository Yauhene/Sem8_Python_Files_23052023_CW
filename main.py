from ph import *
from menu import *

# spis = ["123", "324"]
# data = open('test.txt', 'w')
# data.writelines(spis)

fileContent = readFile('phones.txt')
prAbonents(readFile('phones.txt'))

mainMenu()