import sqlite3
import random

def véletlen():
    vél=random.Random()
    return vél.randrange(2)

def rekord(list,x):
    return list[x]

def adat(list,x,y):
    return list[x][y]


base=sqlite3.connect("szavak.db")
t=base.cursor()
adatok=t.execute("Select szó,mondat1,mondat2,mondat3,mondat4 from szavmon")
datas=[list(adat) for adat in adatok]
szám=[]
szám.append(véletlen())
print(szám)
print(adat(datas,szám[0],0))#szó#
print(adat(datas,szám[0],1))#mondat1#
print(adat(datas,szám[0],2))#mondat2#
print(adat(datas,szám[0],3))#mondat3#
print(adat(datas,szám[0],4))#mondat4#

