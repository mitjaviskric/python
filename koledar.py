# -*- coding: utf-8 -*-

# prikaz koledarja za dva dni
# To do: vnos več ljudi naenkrat.

x = 0     # števec
y = 0     # nov števec za jutri

izposojevalna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4", "informacije 1"]
imena = ["Andreja VI", "Maša", "Sara", "Karmen", "Andreja", "Andreja P", "Mateja"]

# seznam za jutri
imena_jutri = imena[:]       # kopiramo seznam
del imena_jutri[0]           # izbrišemo prvo ime
imena_jutri.append(imena[0]) # dodamo na koncu prvo vrednost iz prejšnjega seznama

manjka = input ("Vnesite kdo manjka:")
if manjka != "":             # če [enter] pojdi naprej
    imena.remove(manjka)     # izbrišemo ime, če manjka
    imena_jutri.remove(manjka)   # tisti, ki manjka danes, a ne bo jutri, gre na konec
    imena_jutri.append(manjka)   # na konec

# jutri
manjka_jutri = input ("Vnesite, kdo bo manjkal jutri:")
if manjka_jutri != "":       # če [enter] pojdi naprej
    imena_jutri.remove(manjka_jutri) # izbrišemo ime, če manjka jutri

print ()
print ("Urnik za danes: ")

for delovno_mesto in izposojevalna_mesta:
    print (delovno_mesto, "=>",imena [x])
    x += 1

print ()
print ("Interno delo:")
print (imena [x:(len(imena))]) #izpiše imena, ki so ostala
print ()
print ("Urnik za jutri: ")

for delovno_mesto in izposojevalna_mesta:
    print (delovno_mesto, "=>",imena_jutri [y]) # x so že porabljeni
    y += 1

print ()
print ("Interno delo jutri:")
print (imena_jutri [y:(len(imena_jutri))])
print ()
