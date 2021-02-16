String = input("word:")
print(len(String))
for x in String:
  print(x)

gnirtS= ""
gnirtS+="!"
print(gnirtS)

#len(String)-1 is last letter
#String[0] is first letter
#loop on letters from first to last letter via: for x in range(len(String))
#empty string is gnirtS

for x in range(len(String)):
  gnirtS+=String[len(String)-1-x]

print(gnirtS)                                         
