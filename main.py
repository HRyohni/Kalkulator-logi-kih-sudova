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
