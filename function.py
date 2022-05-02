from math import pow
import numpy as np
from sympy import *

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


def KrivoZagrade(string):
    Lzagrada = 0
    Dzagrada = 0

    for x in string:
        if (x == "("):
            Lzagrada += 1
        if (x == ")"):
            Dzagrada += 1

    if (Lzagrada + Dzagrada) % 2 != 0:
        print("Krivo unesena formula: nedostaju zagrade!")
        return False
    else:
        return True


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


def Provjera(problem, varijable, BrVar):
    while ImaZnakova(problem) == False or KrivoZagrade(problem) == False:# VisakVarijabli(problem,varijable,BrVar) == False:
        problem = input("\nUnesite izraz za računanje. \n & (Konjunkcija), | (Disjunkcija), ~ (Negacija, za negiranje postavite tvrdnju u zagrade), >> (Implikacija), == (Ekvivalencija)\n\n")


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

