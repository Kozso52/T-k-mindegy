import sqlite3
import hashlib

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
    szó=input("Írja be a szót (kilépés esetén nyomjon egy entert): ")
    while szó!="":
        mondat1=input("Adja meg a szóhoz tartozó mondatot:")
        mondat2=input("Adja meg a szóhoz tartozó mondatot:")
        mondat3=input("Adja meg a szóhoz tartozó mondatot:")
        mondat4=input("Adja meg a szóhoz tartozó mondatot:")
        adatokbe(szó,mondat1,mondat2,mondat3,mondat4)
        if szó!="":
            return adatka()

def regisztráció():
    email = input("Írja be az email címét: ")
    jelszó = input("Adjon meg egy jelszót: ")
    biztjelszó = input("Újra a jelszót: ")
    
    if biztjelszó == jelszó:
        enc = biztjelszó.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        
        with open("beléptetőadatok.txt", "a") as f:
            f.write(email + "|" + hash1 + "\n")
        print("Sikeresen regisztrált!")
    else:
        print("A jelszó nem egyezik!\n")

def bejelentkezés():
    email = input("Írja be az email címét: ")
    jelszó = input("Írja be a jelszavát: ")
    auth = jelszó.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    with open("beléptetőadatok.txt", "r") as f:
        adatok = f.readlines()

    for sor in adatok:
        tárolt_email, tárolt_jelszó = sor.strip().split("|")
        if email == tárolt_email and auth_hash == tárolt_jelszó:
            print("Sikeresen bejelentkezett!")
            adatka()
            break
        else:
            print("Sikertelen bejelentkezés!\n")

while 1:
    print("********** Login System **********")
    print("1.Regisztráció")
    print("2.Bejelentkezés")
    print("3.Kilépés")
    
    választás = int(input("Válasszon a lehetőségek közül: "))
    
    if választás == 1:
        regisztráció()
    elif választás == 2:
        bejelentkezés()
    elif választás == 3:
        break
    else:
        print("Rossz válasz!")



