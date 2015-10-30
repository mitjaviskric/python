## OPOZORILO: deluje le, če je število delovnih mest manjše ali enako številu imen!
x = 0     ## števec 
xj = 0    ## nov števec za jutri


delovna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "interno delo", "interno delo 2"]
imena = ["Andreja V. I.", "Masa", "Sara", "Dusanka", "Andreja"]
imena_jutri = imena[:]       #kopiramo seznam
del imena_jutri[0]           #izbrišemo prvo mesto
imena_jutri.append(imena[0]) #dodamo na koncu prvo vrednost iz prejšnjega seznama

print ()
print ("Urnik za danes: ")

for delovno_mesto in delovna_mesta:
    print (delovno_mesto, "=>",imena [x])
    x += 1
    
print ()
print ("Urnik za jutri: ")

for delovno_mesto in delovna_mesta:
    print (delovno_mesto, "=>",imena_jutri [xj]) ## d so že porabljeni
    xj += 1
    
print ()
