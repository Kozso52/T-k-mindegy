import hashlib
def regisztráció():
    email = input("Írja be az email címét: ")
    jelszó = input("Adjon meg egy jelszót: ")
    biztjelszó = input("Újra a jelszót: ")
    if biztjelszó == jelszó:
        enc = biztjelszó.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("adatok.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("Sikeresen regisztrált!")
    else:
        print("A jelszó nem egyezik! \n")
def bejelentkezés():
    email = input("Írja be az email címét: ")
    jelszó = input("Írja be a jelszavát: ")
    auth = jelszó.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("adatok.txt", "r") as f:
        tárolt_email, tárolt_jelszó = f.read().split("\n")
    f.close()
    if email == tárolt_email and auth_hash == tárolt_jelszó:
         print("Sikeresen bejelentkezett!")
    else:
         print("Sikertelen bejelentkezés! \n")
while 1:
    print("********** Login System **********")
    print("1.Regisztráció")
    print("2.Bejelentkezés")
    print("3.Kilépés")
    vál = int(input("Válasszon a lehetőségek közül: "))
    if vál == 1:
        regisztráció()
    elif vál == 2:
        bejelentkezés()
    elif vál == 3:
        break
    else:
        print("Rossz válasz!")
