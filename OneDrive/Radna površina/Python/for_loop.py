##for i in range(3):
##    print("nesto",i +1, (i +1) * "+")
# Nakon zareza ako stavimo promenljivu napisace nam onoliko puta koliko je u listi
    # Dodati + 1 ako zelimo da krene od 1 pa do naseg broja
        # Zarez pa ovaj deo sto je u zagradi puta bilo koj znak nam ispisuje te znakove 
# 3 argumenta mogu u range  f-ju: prvi= pocetni broj, drugi= poslednji broj, treci: kako da broji

##for x in range(5):
##    for y in range(3):
##        print(f"{x} {y}", end=" . ")
# Ovo je nested loop; end na kraju sluzi da bo spis bio vodoravan a ne vertikalan        

##parni = 0
##for i in range(1,10):
##    if i % 2 == 0:
##        print(i)
##        parni += 1
##print(f"Imamo {parni} parna broja ")
# ZADATAK = trazenje parnih ili neparnih brojeva

##scores = [80, 50, 60, 75]
##sum = 0
##for score in scores:
##    sum += score
##print(sum)
# ZADATAK = sabiranje ili bilo koja matematicka operacija

##files = ['Report.cvs', 'DATA.cvs', 'final.TXT']
##for file in files:
##    print(file.strip().lower().replace('txt', 'cvs'))
# ZADATAK = neka mala manipalicaj tekstom

##sum = 0
##for i in range(1,10+1):
##    sum = 7 * i
##    print(f"7 * {i} = {sum}")
# ZADATAK = mnozenje kao tablica

##rows = 6 # ZAPOCETI UVEK SA PROMENILJIVOM NEKOM MAJKU MU VISE
##for i in range(1, rows + 1):
##    print("*" * i)
# ZADATAK = ZVEZDICE BUDJAVE
    
##names = ['john','maria','','kumar']
##for name in names:
##    if name == '':
##        break
##    print(name)
#Primer sa BREAK

##names = ['john','maria','','kumar']
##for name in names:
##    if name == '':
##        continue
##    print(name)
#Primer sa CONTINUE

##days = ['Mon','Tue','Wen','Thu','Fri','Sat','Sun']
##for day in days:
##    if day in ['Sat','Sun']:
##        continue
##    print(f"Worksday: {day}")
#Primer sa skipovanjem

##emails = [
##    'data@gmail.com',
##    'baraa@outlook.de',
##    'DROP TABLE USERS;',
##    'maria@gmail.com'
##]
##for email in emails:
##    if ';' in email:
##        print('hakovan si')
##        break
##    print(f'idemo dalje: {email}')
#ZADATAK = obican nista spec

##items = [1, 3, 5, 7]
##for i in items:
##    if i % 2 == 0:
##        print(f"Even Nr. Found: {i}")
##        break
##else:
    ##print("All numbers are odd")
#Koriscenje ELSE i BREAK  f-je
    
##names = ['Kamara', 'Tuba', 'Maria', 'Monika']
##for name in names:
##    if name is None:
##        print("Found a missing name")
##        break
##else:
##    print("All names are avaiable")
#ZADATAK = provera liste
    #Break i else koristimo kada proveramo listu
    
##files = ['data1.cvs',
##         'report.pdf',
##        'report2.cvs']

##for file in files:
##    if not file.endswith('.cvs'):
##        print(f"{file} is not a CVS")
##        break
##else:
##    print("All files are good")
#ZADATAK = provera liste
    #Koriscenje ENDWITH() 
    
##file_list = [
##    'report.cvs',   
##    'data.xlsx',
##    'summary.docx',
##    'report.cvs',
##    'data.cvs'
##]
##seen = []
##duplikat = False

##for file in file_list:
##    if file in seen:
##        duplikat = True
##        print(f"Duplikat pronadjen: {file}")
##        break
##    seen.append(file)
##else:
##    print("Nema duplikata, sve je super.")
#ZADATAK = Pronalazenje duplikata

##for x in range(3):
##    for y in range(2):
##        for z in range(2):
##            print(f"({x}, {y}, {z})")
#NESTED LOOPS

##colors = ['red', 'blue', 'green']
##sizes = ['L', 'M', 's']
##for color in colors:
##    for size in sizes:
##        print(f"{color} - Size {size}")
#PRIMER za nested loop

##years = [2026, 2027]
##months = ['Jan', 'Feb']
##days = range(1,29)

##for y in years:
##    for m in months:
##       for d in days:
##            print(f"report_{y}_{m}_{d}.csv")
#PRIMER za nested loop sa 3 promenljive

##tables = ['customors', 'orders', 'products', 'prices']
##columns = ['id','create_date']
##for t in tables:
##    for c in columns:
##        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL;")
#PRIMER za nested loop