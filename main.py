# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!
egyik = int(input('adj egy számot'))
másik = int(input('adj még egy számot'))
harmadik = int(input('adj megint egy számot'))
if egyik > másik < harmadik:
  print (másik, 'a kisebb')
if másik > egyik < harmadik:
  print (egyik, 'a kisebb')
if egyik > harmadik < másik:
  print (harmadik, 'a kisebb')
