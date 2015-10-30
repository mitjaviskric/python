## OPOZORILO: deluje le, če je število imen manjše ali enako številu delovnih mest!
i = 0     ## števec imen
d = 0     ## števec delovnih mest
ij = 0    ## nov števec imen za jutri
dj = 0    ## nov števec delovnih mest za jutri

ime = ["Andreja V. I.", "Masa", "Sara", "Dusanka"]
delovno_mesto = ["izposoja 1", "izposoja 2", "izposoja 3", "interno delo", "interno delo 2"]
delovno_mesto_jutri = delovno_mesto[:]       #kopiramo seznam
del delovno_mesto_jutri[0]                   #izbrišemo prvo mesto
delovno_mesto_jutri.append(delovno_mesto[0]) #dodamo na koncu prvo vrednost iz prejšnjega seznama

print ()
print ("Urnik za danes: ")

for vsakoime in ime:
    print (ime[i], "=>",delovno_mesto [d])
    i += 1
    d += 1
    
print ()
print ("Urnik za jutri: ")

for vsakoime in ime:
    print (ime[ij], "=>",delovno_mesto_jutri [dj]) ## i in d so že porabljeni
    ij += 1
    dj += 1
    
print ()
