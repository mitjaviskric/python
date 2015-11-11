__author__ = 'MIAV'
# -*- coding: utf-8 -*-

import datetime
import calendar
import time

delovna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4", "S1", "S2", "L", "M", "N"]
turnus1 = ["Andreja VI", "Irena", "Sara", "Karmen", "Andreja M", "Suzana Š", "Maja L", "Tomaž M", "Dušanka"]
turnus2 = ["Sabina", "Katja", "Mateja", "Anja", "Janez", "Tomaž Mi", "Maja M", "Suzana HP", "Maša", "Igor"]
odsotni1 = []
odsotni2 = []

x=1
while x != 0:
    manjka=input("Vnesite kdo manjka:")
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

print("Turnus1", turnus1)
print("Odsotni:", odsotni1)
print("Turnus2", turnus2)
print("Odsotni:", odsotni2)
