f = open("latest.log", "r")
for x in f:
  if "AUCTION" in x:
    print(x) 
    f2 = open("auctions.txt", "r")
    foundInFile = False
    for x2 in f2:
      if x in x2:
        foundInFile = True
    f2.close()
    if foundInFile == False:
      f2 = open("auctions.txt", "a")
      f2.write(x)
      f2.close()


f.close()