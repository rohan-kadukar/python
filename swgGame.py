import random
print("s:Snake,w:Water,g:Gun")
cs=0
ms=0
i=1
while i<=10:
  i=i+1
  lst=["s","w","g"]
  cc=random.choice(lst)
  # print(cc)
  mc=str(input("Enter s/w/g: "))
  # print(mc)
  if cc=="s" and mc=="w":
    cs=cs+1
    # print("Computer win")
  elif cc=="s" and mc=="s":
    cs=cs+1
    ms=ms+1
    # print("Tie")
  elif cc=="s" and mc=="g":
    ms=ms+1
    # print("You win")
  elif cc=="w" and mc=="s":
    ms=ms+1
    # print("You win")
  elif cc=="w" and mc=="w":
    cs=cs+1
    ms=ms+1
    # print("Tie")
  elif cc=="w" and mc=="g":
    cs=cs+1
    # print("Computer win")
  elif cc=="g" and mc=="s":
    cs=cs+1
    # print("Computer win")
  elif cc=="g" and mc=="w":
    ms=ms+1
    # print("You win")
  elif cc=="g" and mc=="g":
    cs=cs+1
    ms=ms+1
    # print("Tie")
  else:
    print("You Enter Wrong Choice")
  
  print(f"Computer entered [{cc}] & You entered [{mc}]")
  
print("Game Over")
print(f"Computer score is {cs} and your score is {ms}")
if cs>ms:
  print("Computer is Winner.")
elif cs<ms:
  print("You are Winner.")
else:
  print("It's tie")

