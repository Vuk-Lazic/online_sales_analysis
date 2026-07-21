"""
count = 1
while count <= 5:
    print(count)                                           #PRIMER PETLJE KOJA SE PONAVLJA DOK JE BROJ MANJI ILI JEDNAK OD 5
    count += 1
"""

"""
pitanje = input("Unesite vas odgovor: ")
while pitanje != 'yes':
    print("Pogresan odgovor")                              #PRIMER PETLJE KOJA SE PONAVLJA DOK KORISNIK NE UNESU "yes"
    pitanje = input("Unesite vas odgovor: ")
"""

"""
while True:
    ans = input("Unesite vas odgovor: ")
    if ans == "yes":
        break                                              #PRIMER PORIMER ISTI KAO GORE SAMO SA WHILE TRUE
print("hvala")
"""

"""
pokusaj = 0
while pokusaj < 3:
    pitanje = input(f"Pokusaj {pokusaj + 1} od 3. Da li se slazemo: ")
    if pitanje.lower() == "da":
        print("na istoj smo strani")
        break                                                                #PRIMER PETLJE KOJA SE PONAVLJA DOK KORISNIK NE UNESU "da" ILI DOK NE ISKORISTI SVA 3 POKUSAJA
    pokusaj += 1
if pokusaj == 3:
    print("3 pokusaj si iskoristio")
"""