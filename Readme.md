

# Kalkulator logičkih sudova

[TOC]

## *Uvodno o logici u životu*

Logika se primjenjuje u našem svakodnevnom životu, naime logika nam služi kao nekakav alat ispravnog razmišljanja. Logika nam je ključan dio bili kakvog razmišljanja, preko logike dolazimo do činjenica i tako dolazimo do zaključaka. Bez logike svaka tvrdnja može biti istinita i lažna, došli bi do trenutka oko čega se nitko ne bi mogao složiti. Naravno ne možemo koristiti logiku u svakom odabiru u našem životu pogotovo ako dolazi do pitanja ljudskih osjećaja i mišljenja. 

------



------

## *Logika sudova*

Logika sudova sama posebi je jedan od najprirodnijih formuliranih teorija. Odnosi se na osnovnom matematičkom problemu kako razjasniti istinitu tvrdnju od lažne tvrdnje. Pri korištenju logike promatramo oblik postavljene rečenice a ne njen sadržaj, sadržaj je relativan ako se rečenica ne može proglasit kao sud. Sud sam po se sebi je neka tvrdnja koja je istinita ili lažna ali ne može biti oboje u isto vrijeme. Razjasnimo razliku između suda i obične rečenice:

> Jedan je jednako nula.      Ova rečenica nam je lažan sud.                    

> Jedan plus jedan je dva.      Ova rečenica je istinit sud.

> Kako si?      Ova rečenica nije sud, jer nema nikakvu tvrdnju koju možemo proglasiti istinitom ili  lažnom.

------

### *Složeni sudovi*

Već smo naveli što je sud i definirali smo par jednostavnijih sudova, pomoću tih jednostavnijih sudova i veznika (i, ili, ako) gradimo složene sudove. S složenim sudovima ne gledamo samo njihovu točnost, nego proučavamo i logičko zaključivanje jeli njihov odnos konkretan ili ne. Prikazat ćemo par primjera: 

> Ako si nabavio karte za bus.                              

> Nabavio sam karte. 

> ______________________________

> Idemo na putovanje.

>  

Ovaj logički sud se može zapisat još i na ovaj način. 

> A → B

> A 

> _________________________

> B

Odnos među sudovima je konkretno prikazan, veznik ako povezuje dva suda. Sud **Ako si nabavio karte za bus(A)** je direktno povezan kao pred uvjet za putovanje. **Nabavio sam karte(B)** je radnja koja je prikazala da je uvjet ispunjen. I na kraju je prikazano kako je pred uvjet ispunjen i da se radnja izvršila i da zbog toga **Idemo na putovanje(A).**

------

### *Formalne teorije logike sudova*

U logici sudova definiramo formalne teorije, definirat ćemo što znači zadati neku teoriju. Počinjemo od nekog broja pojmova koji se ne definiraju, a zovu se osnovni pojmovi. Preko toga smo zadali jezik teorije. Pomoću tih osnovnih pojmova dodjeljujemo tvrdnje istinitosti i laži. Tvrdnje čiju istinitost ne dokazujemo zovu se *aksiomi.* Svaku novu zadanu tvrdnju zaključujemo na osnovu aksioma i tvrdnje koje smo već dokazali. Aksiom mora zadovoljavat sljedeća tri principa:

- a) **konzistentnost**, tj. iz sistema aksioma se ne smije moći dokazati istovremeno neka tvrdnja i njena negacija; 

- b) **potpunost**, tj. svaka tvrdnja, ili njena negacija, je dokaziva u danom sistemu aksioma; 

- c) **nezavisnost**, tj. niti jedan aksiom se ne može dobiti kao posljedica ostalih.

------

------

## *Jezik logike sudova*

U ovom dijelu definiramo osnovne znakovne teorije logike sudova. Za deklariranje sudova koristimo velika slova **alfabeta.** 

*Definicija:*

Po dogovoru smatramo da skup svih riječi proizvoljnog alfabeta sadrži praznu riječ, tj. prazan niz simbola. Najvažnija operacija na skupu riječi je ***konkatenacija\***.

Konkatenacija je važna binarna operacija koja se definira na sljedeći način; 

Zamislimo da imamo riječi **A** i **B**. Recimo da je **B** podriječ rijči **A i** ako postoje riječi **C** i **D** možemo zaključit da je **A=BCD**.

Navodimo neki primjer alfabeta:

Neka nam je A<sub> 1</sub> = {α, β}. 

Neke riječi tog alfabeta su npr. ααα, αβαβββ, ααββααβ.

Iz riječi ααββ i ββαβ konkatenacijom dobivamo riječi ααββββαβ.

  

------

## Alfabet logike sudova

Alfabet logike sudova je unija skupova **A1**, **A2** i **A3**, pričemu je:

> **A<sub> 1</sub> =** {Q, P, R...}  => prebrojiv skup čije elemente nazivamo **propozicionalne varijable**.

> **A<sub> 2</sub> =** {¬, ∧, ∨, →, ↔} => skup **logičkih veznika**.

> **A<sub> 3</sub> =** {(, )} => skup pomoćnih simbola(**zagrade**) 

U skupu **A<sub> 1</sub>** reprezentira znakove koje nazivamo **propozicionalne varijable**, znakove označavamo s velikim slovima alfabeta i od njih tvorimo forme.

Skup **A<sub> 2</sub>** prikazuje logičke veznike koje koristimo za deklariranje odnosa među skupovima.

Od veznika imamo:

- **¬ negaciju**(ne)
- **∧ konjukciju**(i)
- **∨ disjunkciju**(ili)
- **→ kondicional**(implikacija)
- **↔ bikondicional**(ekvivalencija)  

Unutar skupa *A<sub> 3</sub>* predstavlja pomoćne simbole koji su ubiti samo zagrade.

------

## *Atomarna formula*

Atomarne formule se odnose na svaku propozicionalnu varijablu, pojam ove formule definiramo induktivno:

-  svaka atomarna formula je formula; 
-  ako su A i B formule tada su i riječi (¬A), (A∧B), (A∨B), (A → B) i (A ↔ B) također formule; 
-  riječi alfabeta logike sudova je formula ako je nastala primjenom konačno mnogo koraka prijašnjih uvjeta 

**Važno je za naglasit:**

Ako primijetimo da u prethodnoj definiciji A i B nisu formule već oznake za formule, tj. to nisu simboli jezika već su meta-simboli. Po dogovoru ćemo s velikim slovima (npr. **A**, **B**, **C**, **F**, **G**, **F<sub> 1</sub>**, **F<sub> 2</sub>**, . . .) označavati formule.

Za propozicionalne varijable upotrebljavat ćemo oznake **P, Q, R, S.**

------

------

## Interpretacija

U prethodnim definicijama smo definirali samo sintaksu logike sudova. U ovom djelu ćemo definirati semantiku, definirati što znači da je neka formula istinita, odnosno neistinita.

*Definicija*:

Svako preslikavanje sa skupa svih propozicionalnih varijabli u skup {0, 1}, tj. I : {P<sub> 0</sub>, P<sub> 1</sub>, . . .} → {0, 1}, nazivamo interpretacija. Ako je preslikavanje definirano na podskupu skupa propozicionalnih varijabli tada kažemo da je to parcijalna interpretacija. Kažemo da je parcijalna interpretacija I adekvatna za formulu A(P<sub> 1</sub>, . . . , P<sub> n</sub>) ako je funkcija I definirana na P<sub> i</sub> za sve i = 1, . . . , n.

*Definicija:*

Neka je I interpretacija (totalna ili parcijalna). Ako se radi o parcijalnoj interpretaciji I smatramo da je I adekvatna za formule na kojima se definira njena vrijednost. Tada vrijednost interpretacije I na proizvoljnoj formuli definiramo induktivno: 

>  I(¬A) = 1           ako i samo ako     I(A) = 0; 

>  I(A ∧ B) = 1       ako i samo ako     I(A) = 1 i I(B) = 1; 

>  I(A ∨ B) = 1       ako i samo ako     I(A) = 1 ili I(B) = 1; 

>  I(A → B) = 1      ako i samo ako     I(A) = 0 ili I(B) = 1;

>  I(A ↔ B) = 1      ako i samo ako     I(A) = I(B).

Za preglednost interpretacije koristimo tablicu koja se naziva u **semantička tablica**.

Preko tablice prijašnji izrazi se interpretiraju na sljedeći način:

|  P   |  Q   |  ¬P  | P ∧ Q | P ∨ Q | P→Q  | P↔Q  |
| :--: | :--: | :--: | :---: | :---: | :--: | :--: |
|  1   |  1   |  0   |   1   |   1   |  1   |  1   |
|  1   |  0   |  0   |   0   |   1   |  0   |  0   |
|  0   |  1   |  1   |   0   |   1   |  1   |  0   |
|  0   |  0   |  1   |   0   |   0   |  1   |  1   |

____

## Normalne forme 

 

Atomarnu formulu i njezinu negaciju nazivamo **literal**. Formulu oblika A<sub> 1</sub> ∧ A<sub> 2</sub> ∧ . . . ∧ A<sub> n</sub> nazivamo konjunkcija (A<sub> i</sub> su proizvoljne formule). Formulu oblika A<sub> 1</sub> ∨ A<sub> 2</sub> ∨ . . . ∨ A<sub> n</sub> nazivamo disjunkcija. Prema tome vrijedi sljedeće:

- **Konjunktivna normalna forma** je konjunkcija elementarnih disjunkcija. 
- **Disjunktivna normalna forma** je disjunkcija elementarnih konjunkcija.

Normalne forme mogu iskazati na 4 načina:

- **ispunjiva** - ako se unutar interpretacije nalazi barem jedna netočna tvrdnja
- **oboriva** - ako se unutar interpretacije nalazi barem jedna netočna tvrdnja 
- **tautologija** - ako su sve tvrdnje unutar interpretacije istinite
- **antitautologija** - ako su sve tvrdnje unutar interpretacije lažne





____

## Općenito o programu

Programski dio našeg projekta smo izvršili pomoću programskog jezika ***python*** zbog njegovog "prisilnog" urednog pisanja koda, jednostavnih sintaksih i zbog našeg dobrog poznavanja python jezika.   

Program se sastoji od dvije datoteke  ***function.py***, u kojoj se nalaze sve funkcije koje čine kod funkcionalnim i ***main.py*** u kojem pozivamo funkcije. Kroz ostatak dokumentacije prikazat ćemo sve funkcije unutar našeg programa, dok će detaljan opis biti u videozapisu.

____

### Function.py

Function.py je datoteka unutar našeg programa koja sadrži funkcije za izvršenje rada našeg programa. Sastoji se od 3 biblioteke:

- **math**
  - Iz math biblioteke smo koristili **pow** naredbu za eksponencijalno povećavanje semantičke tablice
- **sympy** 
  - Iz sympy biblioteke smo koristili **eval()** koji nam služi za procjenu proizvoljnih python izraza iz unosa koji se temelji na nizovima ili prevedenom kodu 
- **numpy**
  - Također smo uveli cijelu **numpy** biblioteku kako bi spremili vrijednosti unutar polja

```python
from math import pow
import numpy as np
from sympy import *

def inverzKNF(polje, varijable, rjesenje, brVar):
def KNF (polje, varijable, rjesenje, brVar):
def DNF(polje, varijable, rjesenje, brVar):
def ImaZnakova(String):    
def KrivoZagrade(string):
def VisakVarijabli(string, varijable, PropVar):
def Racunanje(problem, varijable, polje,PropVar,rjesenje):
def IspisMogucnosti(polje,PropVar,varijable):
def ispisTablice(Vel,polje):
def Provjera(problem, varijable, BrVar):
def UpisPropVar(varijable, brVar):
def pojam(rjesenje):
```

*Collapsani* program

____

#### inverzKNF

```python
def inverzKNF(polje, varijable, rjesenje, brVar):
  polje2 =[]
  for x in range (len(polje)):
   polje2.append(str(polje[x]))

  newarr = np.array_split(polje2, brVar)
  for x in range(len(newarr[0])):
    for y in range(brVar):
      if newarr[y][x] == "False":
        newarr[y][x] = varijable[y]
      else:
        newarr[y][x] = varijable[y].lower()
  
  #Savršena KNF
  print()
  print("Savršena KNF:", end = ' ')
  counter = 0
  for x in rjesenje:
    if x == 0:
      counter += 1
  count = 0

  for x in range(len(rjesenje)):
    if rjesenje[x] == 0:
      count += 1
      
      print("(", end = '')
      for var in range(len(varijable)):
        if newarr[var][x].isupper():
          print(newarr[var][x], end = '') 
        else:
          print("!", end = '')
          print(newarr[var][x].upper(), end = '')
        
        if var != len(varijable) - 1:
          print("&", end = '')
      
      if  count != counter:
        print(")|", end = '')
      else:
        print(")", end = '')
  
  print()
```

____

#### KNF

```python
def KNF (polje, varijable, rjesenje, brVar):
  polje2 =[]
  for x in range (len(polje)):
    polje2.append(str(polje[x]))

  newarr = np.array_split(polje2, brVar)
  for x in range(len(newarr[0])):
    for y in range(brVar):
      if newarr[y][x] == "False":
        newarr[y][x] = varijable[y]
      else:
        newarr[y][x] = varijable[y].lower()
  
  #KNF
  print("\n")
  print("KNF:", end = ' ')
  counter=0
  for x in rjesenje:
    if x == 0:
      counter += 1
  count = 0

  for x in range(len(rjesenje)):
    if rjesenje[x] == 0:
      count += 1
      
      print("(", end = '')
      for var in range(len(varijable)):
        if newarr[var][x].islower():
          print(newarr[var][x].upper(), end = '') 
        else:
          print("!", end = '')
          print(newarr[var][x], end = '')
        
        if var != len(varijable) - 1:
          print("|", end = '')
      
      if  count != counter:
        print(")&", end = '')
      else:
        print(")", end = '')
```

____

#### DNF

```python
def DNF(polje, varijable, rjesenje, brVar):
  polje2 =[]
  for x in range (len(polje)):
    polje2.append(str(polje[x]))
  newarr = np.array_split(polje2, brVar)
  
  #newarr array in string array
  for x in range(len(newarr[0])): # postavlja negativne oznake
    for y in range(brVar):     
      if newarr[y][x] == "True":
          newarr[y][x] = varijable[y]
      else:    
        #save negativne varijable
        for z in range(len(varijable)):
          if newarr[z][x] == "False":
            newarr[z][x] = varijable[z].lower()
            
        
  #DNF
  counter = 0
  for x in rjesenje:
    if x == 1:
      counter += 1
  count = 0
  
  print("DNF:", end = ' ')
  for x in range(len(rjesenje)):
    if rjesenje[x] == 1:
      count += 1
      
      print("(", end = '')
      for var in range(len(varijable)):
        if newarr[var][x].islower():
          print("!", end = '')
          print(newarr[var][x].upper(), end = '') 
        else:
          print(newarr[var][x], end = '')
        
        if var != len(varijable) - 1:
          print("&", end = '')
      
      if  count!= counter: 
        print(")|", end = '')
      else:
        print(")", end = '')

```

____

#### ImaZnakova 

```python
def ImaZnakova(string):
    count = 0
    for x in string:
        if (x == '&' or x == '|' or x == '~' or x == '>' or x == '='):
            count += 1
    if (count < 1):
        print("Krivo unesena formula: nedostaju logicki veznici!")
        return False
    else:
        return True
```

____

#### KrivoZagrade 

```python
def KrivoZagrade(string):
    Lzagrada = 0
    Dzagrada = 0

    for x in string:
        if (x == "("):
            Lzagrada += 1
        if (x == ")"):
            Dzagrada += 1
    #print(Lzagrada, "  ", Dzagrada, " =>", ((Lzagrada + Dzagrada) % 2))

    if (Lzagrada + Dzagrada) % 2 != 0:
        print("Krivo unesena formula: nedostaju zagrade!")
        return False
    else:
        return True
```

____

####  VisakVarijabli

```python
def VisakVarijabli(string, varijable, PropVar):
    count = 0
    for slovo in string:
        if slovo == '&' or slovo == '|' or slovo == '~' or slovo == '>' or slovo == '=' or slovo == '(' or slovo == ')':
            continue

        if slovo in varijable: # Provjera varijabli
            count += 1
            break # Označava samo jednom
        else:
            count -= 1
            break # Označava samo jednom
    print(count)

    if count != PropVar:
        print("Krivo unesena formula: visak/manjak/nedostaje propozicionalnih varijabli!")
        return False
    else:
        return True
```

____

####  Racunanje

```python
def Racunanje(problem, varijable, polje,PropVar,rjesenje):
    print("\nRješenje složenog logičkog suda:")
    newarr = np.array_split(polje, PropVar)
    
    for stanje in range(len(newarr[0])):  # Broj puta stanja varijabla
        for varijabla in range(len(varijable)):  # Broj puta varijabla
            if bool(newarr[varijabla][stanje]) == True:
               x = true
            else:
               x = false
            globals()[chr(65 + varijabla)] = x
     
        print(str(eval(problem))[0:1]) # uzme prvo slovo
        rjesenje.append(bool(eval(problem)))
       
      #print(eval(rjesenje))
    return rjesenje

```

_____

#### IspisMogucnosti

```python
def IspisMogucnosti(polje,PropVar,varijable):
    newarr = np.array_split(polje, PropVar)
    for x in varijable:
        print(x, end = '\t')

    print()
    print("- " * len(varijable) * 3)

    for i in range(len(newarr[0])):  
        for x in newarr:
            print( str(x[i])[0:1], end='\t')
        print()
    print()
```

____

#### ispisTablice

```python
def ispisTablice(Vel,polje):
    # Razmak je npr. TNTN -> razmak je 1 , TTNN -> razmak je 2
    razmak = int(pow(2, Vel))  # Za zadnji korak/stupac
    tocno = True
    Vstupca = razmak

    for redak in range(Vel):
        for stupac in range(Vstupca):
            for y in range(Vel):
                while len(polje) < Vstupca * (y + 1):
                    if tocno == True:
                        for x in range(int(razmak / 2)):
                            polje.append(True)
                        tocno = False
                    else:
                        for x in range(int(razmak / 2)):
                            polje.append(False)
                        tocno = True
                razmak /= 2
```

____

#### Provjera 

```python
def Provjera(problem, varijable, BrVar):
    while ImaZnakova(problem) == False or KrivoZagrade(problem) == False: # VisakVarijabli(problem,varijable,BrVar) == False
        problem = input("\nUnesite izraz za računanje. \n & (Konjunkcija), | (Disjunkcija), ~ (Negacija, za negiranje postavite tvrdnju u zagrade), >> (Implikacija), == (Ekvivalencija)\n\n")
```

____

#### UpisPropVar

```python
def UpisPropVar(varijable, brVar):

    # Uvjeti za ispravan odabir propozicionalnih varijabli
    while brVar < 1 or brVar > 9:
        if brVar < 1 or brVar > 9:
            print("Pogrešan unos!\n")
            brVar = int(input("Ponovno unesite broj propozicionalnih varijabli: "))

    for x in range(brVar):
        varijable.append(chr(65 + x))
        # ASCII vrijednost za A je 65, nadovezivanje varijabli na ASCII vrijednosti

    print("Propozicionalne varijable:", varijable, "\n\n")

    return varijable
#take string replace whereever there is "!" replace all letters in () negative

```

____

#### pojam

```python
def pojam(rjesenje):
  tocne,netocne = 0, 0

  print()

  for x in rjesenje:
    if x == True:
      tocne += 1
    else:
      netocne += 1

  if tocne == len(rjesenje):
    print("Tautologija")

  if netocne == len(rjesenje):
    print("Antitautologija")
  
  if tocne > 0:
    print("Ispunjiva")
  
  if netocne > 0:
    print("Oboriva")
```

____

## main. py

***Main.py*** je programska datoteka preko koje pokrećemo ***Kalkulator logičkih sudova***. Unutar datoteke pozivao sve već navedene funkcije iz ***function.py***(pomoću *from function import*) u jedan smisleni program.  

```python
# Kalkulator logike sudova

import numpy as np
from sympy import *
from function import *

polje = []
varijable = []
rjesenje=[]

PropVar = int(input("Unesite željeni broj propozicionalnih varijabli: ")) # upis broja varijabli
UpisPropVar(varijable, PropVar) # upis varijabli
ispisTablice(int(PropVar),polje) # kreira polje vrijednosti
IspisMogucnosti(polje,PropVar,varijable) # ispisuje tablice
problem = input("\nUnesite izraz za računanje. \n & (Konjunkcija), | (Disjunkcija), ~ (Negacija), >> (Implikacija), == (Ekvivalencija)\n\n")
Provjera(problem, varijable, PropVar) # provjerava unos
rjesenje = Racunanje(problem, varijable, polje,PropVar,rjesenje) # racuna rjesenje

#invert rjesenje
for x in range(len(rjesenje)):
    if rjesenje[x] == -2 :
        rjesenje[x] = False
    elif rjesenje[x] == -1:
        rjesenje[x] = True

print("\nRješenje:", rjesenje, "\n\n")
DNF(polje, varijable, rjesenje, PropVar) # ispisuje DNF
KNF(polje, varijable, rjesenje, PropVar) # ispisuje KNF 
inverzKNF(polje, varijable, rjesenje, PropVar) # ispisuje inverz KNF 
pojam(rjesenje) # ispisuje pojam
```

____

## Korišteni software

https://miro.com/online-whiteboard/"Online-Whiteboard"

https://code.visualstudio.com/"Code-editor"

https://replit.com/"Online code-editor"

https://clickup.com/"To Do aplikacija za organizaciju rada"

____

## Literatura

https://www.youtube.com/watch?v=lxWT8hDJQyQ&list=PLgWzsQkBWNM55KH6q4HSerPGW5F2faf4Z "Matina Matika- Najjednostavnja logika. Sve o sudovima"

https://pypi.org/project/tabulate/ "Python-tabulate"

https://www.logicthrupython.org/ "Mathematical Logic through Python"

https://www.tutorialspoint.com/sympy/sympy_logical_expressions.htm "SymPy - Logical Expressions"

https://www.adamsmith.haus/python/answers/how-to-convert-an-int-to-a-char-in-python "Python help"

https://docs.sympy.org/latest/modules/logic.html "SymPy-syntax"

http://www.mathos.unios.hr/logika/Logika_skripta.pdf "Mladen Vuković MATEMATICKA LOGIKA 1"

https://numpy.org/ "NumPy"

____

***Članovi:***

**Filippo Bubić**, 

**Leo Matošević**,

**Stevan Čorak**, 
