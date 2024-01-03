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
    for adatok in t.execute("Select szó,mondat1 from szavmon"):
        print(adatok)
    adatbázis.close()
    
def adatka():
    global szó
    global mondat1
    global mondat2
    global mondat3
    global mondat4
    szó=input("szó: ")
    while szó!="":
        mondat1=input("Mondat:")
        mondat2=input("Mondat:")
        mondat3=input("Mondat:")
        mondat4=input("Mondat:")
        if szó!="":
            return adatka()
adatka()
adatokbe(szó,mondat1,mondat2,mondat3,mondat4)
