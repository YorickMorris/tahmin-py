import random
import sys
import os
from fastapi import FastAPI,Body

#workingdirectory=os.getcwd()
#Python method getcwd() returns current working directory of a process.
#sys.argv() is an array for command line arguments in Python.
#print('Link: ',sys.argv[0])
app=FastAPI()
sayilar = range(0, 100)
sayi = random.choice(sayilar)
print(sayi)
secim = None

@app.get("/tahmin")
def call(t:int):
    if t==sayi:
        return{
            "cevap":"dogru"
        }
    else:
        return{
            "cevap":"yanlis"
        }

@app.post("/tahmin")
def call1(b:dict=Body(...)):
    sayi=b["sayi"]
    return b
# for i in range(10):
#     print(str(i + 1) + ". denemeniz : ")
#     #secim = input()
#     secim=22
#     #secim=sys.argv[1]
#     if(str(secim) == str(sayi)):
#         print("Tebrikler dogru tahmin !")
#         break

#     else:
#         print("Bilemediniz")
