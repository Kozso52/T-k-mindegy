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
alma=t.execute("Select szó from szavmon")
szavak=[list(adat) for adat in alma]
szám=[]
szám.append(véletlen())


##print(adat(datas,szám[0],0))#szó#
##print(adat(datas,szám[0],1))#mondat1#
##print(adat(datas,szám[0],2))#mondat2#
##print(adat(datas,szám[0],3))#mondat3#
##print(adat(datas,szám[0],4))#mondat4#


if adat(datas,szám[0],0)==adat(datas,szám[0],0):
    print(adat(datas,szám[0],1))
    kiv=input("Ön melyik szóra gondol?: ")
    if kiv==adat(datas,szám[0],0):
        print("Ez a jó")
    else:
        print("Ez sajnos helytelen. Itt a következő mondat:",adat(datas,szám[0],2))
        kiv=input("Az előző szó helytelen volt. Kérem a szót!")
        if kiv==adat(datas,szám[0],0):
            print("Ez a jó")
        else:
            print("Ez sajnos helytelen. Itt a következő mondat:",adat(datas,szám[0],3))
            kiv=input("Az előző szó helytelen volt. Kérem a szót!")
            if kiv==adat(datas,szám[0],0):
                print("Ez a jó")
            else:
                print("Ez sajnos helytelen. Itt a következő mondat:",adat(datas,szám[0],4))
                kiv=input("Az előző szó helytelen volt. Kérem a szót!")
                if kiv==adat(datas,szám[0],0):
                    print("Ez a jó")
                else:
                    print("Ön baszta a szó",adat(datas,szám[0],0))
        
    
