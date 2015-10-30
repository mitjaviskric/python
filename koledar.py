i = 0     ## stevec imen
d = 0     ## stevec delovnih mest
ij = 0    ## nov stevec imen za jutri
dj = -1   ## stevec delovnih mest za jutri z novim razporedom, premaknjenim za eno

ime = ["Andreja", "Masa", "Sara"]
delovno_mesto = ["izposoja 1", "izposoja 2", "interno delo"]

print ()
print ("Urnik za danes: ")

for vsakoime in ime:
    print (ime[i], "=>",delovno_mesto [d])
    i += 1
    d += 1
    
print ()
print ("Urnik za jutri: ")

for vsakoime in ime:
    print (ime[ij], "=>",delovno_mesto [dj])
    ij += 1
    dj += 1

print ()
