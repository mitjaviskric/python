x = 0     # števec 
y = 0     # nov števec za jutri

izposojevalna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4", "informacije 1"]
imena = ["Andreja V. I.", "Masa", "Sara", "Karmen", "Andreja", "Andreja P.", "Mateja"]
manjka = input ("Vnesite kdo manjka:")
imena.remove(manjka)
imena_jutri = imena[:]       #kopiramo seznam
del imena_jutri[0]           #izbrišemo prvo mesto
imena_jutri.append(imena[0]) #dodamo na koncu prvo vrednost iz prejšnjega seznama

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
