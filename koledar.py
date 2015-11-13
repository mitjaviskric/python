__author__ = 'MIAV'
# -*- coding: utf-8 -*-

import datetime
import calendar
import time
import locale
locale.setlocale(locale.LC_ALL, "sl_SI")
import os
os.environ['TZ'] = 'Europe/Ljubljana'

delovna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4", "S1", "S2", "L", "M", "N"]
turnus1 = ["Andreja VI", "Irena", "Sara", "Karmen", "Andreja M", "Suzana Š", "Maja L", "Tomaž M", "Dušanka"]
turnus2 = ["Sabina", "Katja", "Mateja", "Anja", "Janez", "Tomaž Mi", "Maja M", "Suzana HP", "Maša", "Igor"]
odsotni1 = []
odsotni2 = []

# določimo teden
# datum = time.strftime ("%d.%m.%Y")
teden = int(time.strftime("%V"))
# ura = time.strftime ("%H:%M:%S")

# pravila za izmene
if teden % 2 == 0:
    print ("dopoldne turnus1, popoldne turnus2")
else:
    print ("dopoldne turnus2, popoldne turnus1")

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
print("Odsotni iz turnusa 1: ", odsotni1)
print ()
print("Turnus 2: ", turnus2)
print("Odsotni iz turnusa 2: ", odsotni2)
