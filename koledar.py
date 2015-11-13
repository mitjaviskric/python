# -*- coding: utf-8 -*-
#!/usr/bin/env python3
__author__ = 'MIAV'

import datetime
import calendar
import time
import locale
locale.setlocale(locale.LC_ALL, "sl_SI")
import os
os.environ['TZ'] = 'Europe/Ljubljana'
from dateutil import easter

delovna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4", "S1", "S2", "L", "M", "N"]
turnus1 = ["Andreja VI", "Irena", "Sara", "Karmen", "Andreja M", "Suzana Š", "Maja L", "Tomaž M", "Dušanka"]
turnus2 = ["Sabina", "Katja", "Mateja", "Anja", "Janez", "Tomaž Mi", "Maja M", "Suzana HP", "Maša", "Igor"]
odsotni1 = []
odsotni2 = []

# določimo leto
leto = int(time.strftime ("%Y"))
# določimo teden
datum = time.strftime ("%d.%m.%Y")
print (datum)
teden = int(time.strftime("%V"))
# določimo, ali je sobota danes ali jutri
danes = datetime.date.today()
print ("Danes smo", danes)
dan = danes.isoweekday()
print ("Dan v tednu: ", dan)

# ura = time.strftime ("%H:%M:%S")

# določimo praznike
velika_noc = easter.easter(leto)
print ("velika noč: ", velika_noc)

# pravila za izmene
if teden % 2 == 0:
    print ("Dopoldne: Turnus 1")
    print ("Popoldne: Turnus 2")
else:
    print ("Dopoldne: Turnus 2")
    print ("Popoldne: Turnus 1")

# določimo kdo manjka
x=1
while x != 0:
    manjka=input("Vnesite kdo manjka: ")
    if manjka in turnus1:
        turnus1.remove(manjka)
        odsotni1.append(manjka)
        x=2
    elif manjka in turnus2:
        turnus2.remove(manjka)
        odsotni2.append(manjka)
        x=2
    else:
        x=0

print("Turnus 1: ", turnus1)
print("Odsotni iz Turnusa 1: ", odsotni1)
print ()
print("Turnus 2: ", turnus2)
print("Odsotni iz Turnusa 2: ", odsotni2)
