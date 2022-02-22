import random
import sys
import os

workingdirectory=os.getcwd()
#Python method getcwd() returns current working directory of a process.
#sys.argv() is an array for command line arguments in Python.
print('Link: ',sys.argv[0])
sayilar = range(0, 100)
sayi = random.choice(sayilar)
print(sayi)
secim = None


for i in range(10):
    print(str(i + 1) + ". denemeniz : ")
    #secim = input()
    secim=sys.argv[1]
    if(str(secim) == str(sayi)):
        print("Tebrikler dogru tahmin !")
        break

    else:
        print("Bilemediniz")
