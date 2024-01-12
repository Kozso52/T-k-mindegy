import sqlite3
def adatokbe(szó,mondat1,mondat2,mondat3,mondat4):
    adatbázis=sqlite3.connect("szavak.db")
    t=adatbázis.cursor()
    t.execute("CREATE TABLE IF NOT EXISTS szavmon(szó,mondat1,mondat2,mondat3,mondat4)")
    para= """ INSERT INTO szavmon (szó,mondat1,mondat2,mondat3,mondat4)
    VALUES(?,?,?,?,?);"""
    data= (szó,mondat1,mondat2,mondat3,mondat4)
    t.execute(para,data )
    adatbázis.commit()
    adat=t.execute("Select szó,mondat1 from szavmon")
    print(adat.fetchall())
    for adatok in t.execute("Select szó,mondat1,mondat2,mondat3,mondat4 from szavmon"):
        print(adatok)
    adatbázis.close()

print("************Üdvözlöm program szó és mondat megadó részlegén!************")
    
def adatka():
    global szó
    global mondat1
    global mondat2
    global mondat3
    global mondat4
    szó=input("Írja be a szót: ")
    while szó!="":
        mondat1=input("Adja meg a szóhoz tartozó mondatot:")
        mondat2=input("Adja meg a szóhoz tartozó mondatot:")
        mondat3=input("Adja meg a szóhoz tartozó mondatot:")
        mondat4=input("Adja meg a szóhoz tartozó mondatot:")
        adatokbe(szó,mondat1,mondat2,mondat3,mondat4)
        if szó!="":
            return adatka()
adatka()

