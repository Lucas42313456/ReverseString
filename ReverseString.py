String = "trebmir"
print(len(String))
for x in String:
  print(x)

Gnirts= ""
Gnirts+="!"
print(Gnirts)

#len(String)-1 is last letter
#String[0] is first letter
#loop on letters from first to last letter via: for x in range(len(String))
#lege verzameling Gnirts

for x in range(len(String)):
  Gnirts+=String[len(String)-1-x]

print(Gnirts)                                         