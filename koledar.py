## OPOZORILO: deluje le, če je število imen manjše ali enako številu delovnih mest!
d = 0     ## števec delovnih mest
dj = 0    ## nov števec delovnih mest za jutri

imena = ["Andreja V. I.", "Masa", "Sara", "Dusanka"]
delovna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "interno delo", "interno delo 2"]
delovna_mesta_jutri = delovna_mesta[:]       #kopiramo seznam
del delovna_mesta_jutri[0]                   #izbrišemo prvo mesto
delovna_mesta_jutri.append(delovna_mesta[0]) #dodamo na koncu prvo vrednost iz prejšnjega seznama

print ()
print ("Urnik za danes: ")

for ime in imena:
    print (ime, "=>",delovna_mesta [d])
    d += 1
    
print ()
print ("Urnik za jutri: ")

for ime in imena:
    print (ime, "=>",delovna_mesta_jutri [dj]) ## d so že porabljeni
    dj += 1
    
print ()
