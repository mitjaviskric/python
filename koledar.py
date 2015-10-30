## OPOZORILO: deluje le, če je stevilo imen manjše ali enako stevilu delovnih mest!
i = 0     ## stevec imen
d = 0     ## stevec delovnih mest
ij = 0    ## nov stevec imen za jutri
dj = -4   ## stevec delovnih mest za jutri z novim razporedom, premaknjenim za eno

ime = ["Andreja V. I.", "Masa", "Sara", "Dusanka"]
delovno_mesto = ["izposoja 1", "izposoja 2", "izposoja 3", "interno delo", "interno delo 2"]

print ()
print ("Urnik za danes: ")

for vsakoime in ime:
    print (ime[i], "=>",delovno_mesto [d])
    i += 1
    d += 1
    
print ()
print ("Urnik za jutri: ")

for vsakoime in ime:
    print (ime[ij], "=>",delovno_mesto [dj]) ## i in d so ze porabljeni
    ij += 1
    dj += 1

print ()
