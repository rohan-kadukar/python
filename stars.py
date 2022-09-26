print("Hpw Many Rooows You Want")
row = int(input())
print("Enter 0 or 1 for True or False Respectively")
b = input()
c= bool(b)
if c==True:
  for i in range(1,row+1):
    for j in range(1,i+1):
      print("*",end="")
    print()
elif c==False:
  for i in range(row,0,-1):
    for j in range(1,i+1):
      print("*",end="")
    print()