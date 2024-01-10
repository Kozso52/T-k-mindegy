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

print(adat(datas,véletlen(),0))

