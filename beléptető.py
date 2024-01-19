import hashlib

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
            return

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



