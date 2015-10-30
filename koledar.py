x = 0     # števec 
xj = 0    # nov števec za jutri


izposojevalna_mesta = ["izposoja 1", "izposoja 2", "izposoja 3", "izposoja 4"]
ostala_delovna_mesta = ["interno delo 1", "interno delo 2"]
imena = ["Andreja V. I.", "Masa", "Sara", "Karmen", "Andreja", "Andreja P.", "Mateja"]
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
    print (delovno_mesto, "=>",imena_jutri [xj]) # d so že porabljeni
    xj += 1
    
print ()
print ("Interno delo jutri:")
print (imena_jutri [xj:(len(imena_jutri))])
print ()
