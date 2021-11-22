#!/usr/bin/env python3
############################################################################
# Soubor:   main.py
# Datum:    15/11/2021
# Autor:    Ondrej Vilim
############################################################################
from random import randint, choice
import os

############################################################################

print("""
Zadeje volbu:
1) Chcete pracovat se souborem?
2) Chcete vygenerovat náhodný soubor?
""")

volba1=int(input("Zadejte číslo volby: "))

if volba1==1:

    print("""
    Chcete:
    1) Převést soubor na malá písmena
    2) Nahradit znak jiným znakem
    3) Statistiku jednotlivých znaků
    """)
    
    podvolba1=int(input("Zadejte číslo volby: "))
    
    if podvolba1==1:
        soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
        obsah=soubor1.read()
        soubor2=open(input("Zadejte název výstupního souboru: "),"w")
        prepis=obsah.lower()
        vystup=soubor2.write(prepis)
        print("""
        Soubor se přepsal do cílového souboru.
        Soubor je zapsán pouze malými písmeny.
        """)
    
    elif podvolba1==2:

        soubor1=open(input("Zadejte cestu k pracovnímu souboru: "),"r")
        obsah=soubor1.read()
        soubor2=open(input("Zadejte název výstupního souboru: "),"w")
        
        zmenit=input("zadejte znak, který chcete změnit: ")
        nahrada=input("zadejte znak, kterým chcete nahrazovat první znak: ")
        
        if zmenit.isalpha() == True and nahrada.isalpha() == True:
            done=obsah.replace(zmenit.lower(),nahrada.lower()).replace(zmenit.upper(),nahrada.upper()) #Aby nedošlo ke změně velikostí písmen, použil jsem .lower() a .upper()
            vystup=soubor2.write(done)
        
        elif zmenit.isalpha() == True and nahrada.isalpha() == False:
            done=obsah.replace(zmenit.lower(),nahrada).replace(zmenit.upper(),nahrada)
            vystup=soubor2.write(done)
        
        else:
            done=obsah.replace(zmenit,nahrada)
            vystup=soubor2.write(done)

        print("Znak byl úspěšně nahrazen.")
    
    elif podvolba1==3:    
        
        soubor1 = input("Zadejte cestu k pracovnímu souboru: ")
        obsah = open(soubor1,"r")
        soubor2 = input("Zadejte cestu k výstupnímu souboru: ")

        pismena=dict()
        
        while True:
            znak = obsah.read(1).upper()
            if znak == '':
                break
            elif znak in pismena.keys():
                pismena[znak] += 1
            else:
                pismena[znak] = 1

        nej = max(pismena.values())
        for znak in sorted(pismena.keys()):
            if znak.isalpha():
                done=print('{1:8d}| {0} | {2}'.format(znak, pismena[znak], 50 * pismena[znak] // nej * '*'))

    else:
        print("Neplatná volba, ukončuji program!!!")
        




elif volba1==2:
    
    vystupni_soubor=open(input("Zadejte jméno výstupního souboru: "),"w")
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"

    pocet_slov=int(input("Zadejte počet slov pro vygenerovaný soubor: "))

    def gen_slov(minznak=3, maxznak=10):
        vysledek = ""
        pocet = randint(minznak,maxznak)
        zacatek = randint(0,1)
        for i in range(pocet):
            if i % 2 == zacatek:
                vysledek=vysledek + choice(samohlasky)
            else:
                vysledek = vysledek + choice(souhlasky)
        return vysledek    

    def gen_vet(minslov=3, maxslov=12):
        vysledek=""
        for i in range(randint(minslov,maxslov)):
            vysledek = vysledek + gen_slov() + " "
        return vysledek.capitalize()[0:-1]+"."

    vysledek=vystupni_soubor.write(gen_vet())

    print("Náhodná zpráva byla úspěšně vygenerována.")



else:
    print("Neplatná volba, ukončuji program!!!")