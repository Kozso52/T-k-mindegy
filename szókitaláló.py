print("Szia, Üdvözöllek!")
import random
random=random.Random()
keres=""
szólista=['alma','körte','szilva']
print('Szerinted melyikre gondolok:',szólista)
segitlista=[['Gyümölcs','Több fajta van belőle','A betűvel kezdődik','Minden nap egy ... az orvost távol tartja '],['Befőtt is lehet','Fán terem.'],['Hull a ... a fáról','Kerek alakú','Pálinka is van belőle']]

keres=input("Találd ki mire gondolok: ")    
talál=random.choice(szólista)
if talál == 'körte':
    for i in range(len(segitlista[0])):
        print(segitlista[1][i])
        random=input("Válasz:")
        if keres==talál:
            print("Gratulálok! Helyes válasz!, A szó a(z)",talál)
            break
        else:
            print("Nem talált!")
    print('A helyes válasz az alma volt.')
