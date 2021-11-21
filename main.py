#!/usr/bin/env python3
############################################################################
# Soubor:   main.py
# Datum:    15/11/2021
# Autor:    Ondrej Vilim
############################################################################
from random import randint, choice
import os

############################################################################
a 
print("""
Zadeje volbu:
1) Chcete pracovat se souborem?
2) Chcete vygenerovat náhodný soubor?
""")
volba1=int(input("Zadejte číslo volby: "))

if volba1==1:
    soubor1=open(input("Zadejte cestu k pracovnímu souboru: "))
    obsah=soubor1.read()
    soubor2=open(input("Zadejte název výstupního souboru: "),"w")
    print("""
    Chcete:
    1) Převést soubor na malá písmena
    2) Nahradit znak jiným znakem
    3) Statistiku jednotlivých znaků
    """)
    podvolba1=int(input("Zadejte číslo volby: "))
    if podvolba1==1:
        prepis=obsah.lower()
        vystup=soubor2.write(prepis)
        print("""
        Soubor se přepsal do cílového souboru.
        Soubor je zapsán pouze malými písmeny.
        """)
    elif podvolba1==2:
        zmenit=input("zadejte znak, který chcete změnit: ")
        print("Dodělat!!!")
    elif podvolba1==3:
        print("Dodělat!!!")
    else:
        print("Neplatná volba, ukončuji program!!!")
        




elif volba1==2:
    pocet_slov=int(input("Zadejte počet slov pro vygenerovaný soubor: "))
    print(pocet_slov)

else:
    print("Neplatná volba, ukončuji program!!!")